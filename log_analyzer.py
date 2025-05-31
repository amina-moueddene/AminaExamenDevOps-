import os
from datetime import datetime

def analyze_log_file(log_file_path):
    """Analyse le fichier de log et compte les différents niveaux"""
    if not os.path.exists(log_file_path):
        print(f"Erreur: Il {log_file_path} n'existe pas")
        return None
    
    error_count = 0
    warning_count = 0
    info_count = 0
    
    with open(log_file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip().upper()
            if 'ERROR' in line:
                error_count += 1
            elif 'WARNING' in line:
                warning_count += 1
            elif 'INFO' in line:
                info_count += 1
    
    return {
        'errors': error_count,
        'warnings': warning_count,
        'infos': info_count
    }

def create_report(stats, report_file_path):
    """Crée le fichier rapport avec les statistiques"""
    with open(report_file_path, 'w', encoding='utf-8') as file:
        file.write("=== RAPPORT D'ANALYSE DES LOGS ===\n")
        file.write(f"Date d'analyse: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write("-" * 40 + "\n")
        file.write(f"Nombre d'ERREURS: {stats['errors']}\n")
        file.write(f"Nombre de WARNINGS: {stats['warnings']}\n")
        file.write(f"Nombre d'INFOS: {stats['infos']}\n")
        file.write("-" * 40 + "\n")
        file.write(f"Total des événements: {sum(stats.values())}\n")
    
    print(f"Rapport créé: {report_file_path}")

def main():
    log_file = "log.txt"
    report_file = "rapport.txt"
    
    print("🔍 Analyse du fichier de logs en cours...")
    
    stats = analyze_log_file(log_file)
    if stats:
        create_report(stats, report_file)
        print(f"Analyse terminée:")
        print(f"   - Erreurs: {stats['errors']}")
        print(f"   - Warnings: {stats['warnings']}")
        print(f"   - Infos: {stats['infos']}")
        
        # Condition d'échec pour Jenkins (plus de 5 erreurs)
        if stats['errors'] > 5:
            print("ÉCHEC: Plus de 5 erreurs détectées!")
            exit(1)
    else:
        print(" Échec de l'analyse")
        exit(1)

if __name__ == "__main__":
    main()