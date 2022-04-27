import modules.IslaiduIrasas


class PajamuIrasas(modules.IslaiduIrasas.Irasas):
    def __init__(self, suma, siuntejas, papildoma_info):
        super().__init__(suma)
        self.siuntejas = siuntejas
        self.papildoma_info = papildoma_info