from interface.penjual_operation import PenjualOperation

class PenjualController(PenjualOperation):
    
    def menolak_pesanan(self) -> None:
        print("Penjual menolak pesanan karena stok habis")
        
    def menyiapkan_pesanan(sself) -> None:
        print("Penjual menyiapkan pesanna sesuai pilihan pembeli")