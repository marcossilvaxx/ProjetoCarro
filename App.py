from Carro import Carro
from Hibrido import Hibrido

def main():
    carro1 = Hibrido("Preto", "Palio", "1997")
    carro1.carregarBateria() 
    carro2 = Carro("Branco", "Celta", "2001")
    carro2.acelerar()

if __name__ == "__main__":
    main()
