from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Gui', 6)
restaurante_praca.receber_avaliacao('Lais', 7)
restaurante_praca.receber_avaliacao('Emy', 9)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()