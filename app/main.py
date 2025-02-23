import mysql.connector
from mysql.connector import Error

# Configuration de connexion à MySQL (correspondant à docker-compose.yml)
db_config = {
    "host": "mysql",  # Nom du service MySQL défini dans docker-compose
    "user": "root",
    "password": "root",
    "database": "users_db"
}

try:
    # Connexion à MySQL
    connection = mysql.connector.connect(**db_config)

    if connection.is_connected():
        print("✅ Connexion réussie à MySQL")
        
        cursor = connection.cursor()

        # Récupérer la liste des tables
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()

        if not tables:
            print("⚠️ Aucune table trouvée dans la base de données.")
        else:
            print("\n📂 Tables trouvées :")
            for (table_name,) in tables:
                print(f"- {table_name}")

                # Récupérer les colonnes de chaque table
                cursor.execute(f"SHOW COLUMNS FROM {table_name};")
                columns = cursor.fetchall()
                
                print("  🛠️ Colonnes :")
                for col in columns:
                    print(f"    - {col[0]} ({col[1]})")

except Error as e:
    print(f"❌ Erreur lors de la connexion à MySQL : {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("\n🔌 Connexion MySQL fermée.")

