import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, desc, year, when, round

# Defino rrugën e skedarit tuaj të të dhënave (duhet te jete Posts.xml)
DATA_FILE = "Posts.xml" 
# Skedar i madh XML, sigurohuni qe eshte ne ~/Projekti_BigData/Posts.xml

# Konfigurimi i Spark Session (per te lexuar XML)
print("— TENTATIVE PER KRIJIMIN E SPARK SESSION —")
spark = SparkSession.builder \
    .appName("StackOverflowAnswerRate_EN") \
    .master("local[*]") \
    .config("spark.driver.extraJavaOptions", "-Djava.io.tmpdir=/tmp/spark") \
    .config("spark.jars.packages", "com.databricks:spark-xml_2.12:0.18.0") \
    .config("spark.driver.maxResultSize", "4g") # Rritja e limitit per rezultate te medha
    .getOrCreate()

print(f"\nSESIONI I SPARK-UT U KRIJUA ME SUKSES!")
print(f"Spark Version: {spark.version}")
print(f"Master: {spark.conf.get('spark.master')}")

try:
    # ----------------------------------------------------
    # I. LEXIMI I TE DHENAVE (Data Loading)
    # ----------------------------------------------------
    print(f"\nDuke lexuar skedarin e madh: {DATA_FILE}...")
    
    # Spark XML package perdor formatin "xml"
    df = spark.read.format("xml") \
        .option("rowTag", "row") \
        .load(DATA_FILE)
#hadba
    print("\n--- I. EKSPLORIMI I TE DHENAVE (Posts.xml Full) ---")
    df.printSchema()
    
    # ----------------------------------------------------
    # II. ANALIZA E PERQINDJES SE PERGJIGJEVE
    # Përgjigja ndaj pyetjes: "Cila është përqindja e pyetjeve që kanë marrë përgjigje?"
    # ----------------------------------------------------

    # 1. Filtro vetëm Pyetjet (PostTypeId = 1) dhe shto vitin e krijimit
    questions_df = df.filter(col("_PostTypeId") == 1) \
                     .withColumn("Year", year(col("_CreationDate")))

    # 2. Llogarit statistikat (Pyetje totale, Pyetje të Përgjigjura)
    answer_rate_by_year = questions_df.groupBy("Year") \
        .agg(
            count(col("_Id")).alias("Total_Questions"),
            count(when(col("_AnswerCount") > 0, True)).alias("Questions_Answered"),
        ) \
        .filter(col("Year").isNotNull()) \
        .withColumn(
            "Answer_Rate_Percent",
            round((col("Questions_Answered") / col("Total_Questions") * 100), 2)
        ) \
        .orderBy("Year")

    print("\nPERQINDJA E PYETJEVE TE PERGJIGJURA SIPAS VITIT:")
    answer_rate_by_year.show(50)
    
    # Llogaritja e shkallës globale
    total_questions = questions_df.count()
    total_answered = questions_df.filter(col("_AnswerCount") > 0).count()
    overall_rate = (total_answered / total_questions) * 100
    print(f"\nPERQINDJA GLOBALE E PYETJEVE TE PERGJIGJURA: {overall_rate:.2f}%")

except Exception as e:
    # Gabimi ndoshta do të jetë i lidhur me OutOfMemory (OOM) ose PATH_NOT_FOUND.
    print(f"\nNDODHI NJE GABIM GJATE LEXIMIT TE SKEDARIT: {e}")
    print(f"Gabimi i zakonshëm me skedarë kaq të mëdhenj: Kufizimi i kujtesës ose mungesa e skedarit.")

finally:
    # Mbyllni Spark Session
    spark.stop()
    print("\nSesioni i Spark-ut u Mbyll.")
