# Källa: Videor (klasser), (moduler)

import pandas as pd
from .stats_utils import calculate_descriptive_stats

class HealthAnalyzer:    # Gör en klass för att analysera hälso-data.
    
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)     # Laddar in CSV-filen vid start
        print(f"Data laddad: {len(self.df)} rader")
    
    def get_stats(self, columns):   
        return calculate_descriptive_stats(self.df, columns)    # Returnerar statistik med en funktion