class Computador():
    def __init__(self, modelo, gpu_nome, gpu_memoria, cpu_nome, cpu_cores, cpu_clock, memoria_qntGB):
        self.modelo = modelo
        self.gpu = self.GPU(gpu_nome, gpu_memoria)
        self.cpu = self.CPU(cpu_nome, cpu_cores, cpu_clock)
        self.memoria = self.Memoria(memoria_qntGB)
        
    def mostrar_Configuracao(self):
        print(f'Computador: {self.modelo}')
        self.gpu.mostrar_Gpu()
        self.cpu.mostrar_Cpu()
        self.memoria.mostrar_Memoria()
            
    class GPU:
        def __init__(self, nome, memoriaGB):
            self.nome = nome
            self.memoriaGB = memoriaGB
        
        def mostrar_Gpu(self):
            print(f'GPU: {self.nome} - {self.memoriaGB} GB')

    class CPU:
        def __init__(self, nome, cores, clock_ghz):
            self.nome = nome
            self.cores = cores
            self.clock_ghz = clock_ghz
            
        def mostrar_Cpu(self):
            print(f'CPU: {self.nome} - {self.cores} núcleos - {self.clock_ghz} GHz')

    class Memoria:
        def __init__(self, qntGB):
            self.qntGB = qntGB
            
        def mostrar_Memoria(self):
            print(f'Memória: {self.qntGB}GB RAM')
    
pc1 = Computador(modelo='Dell XPS', gpu_nome='NVIDIA RTX 4090', gpu_memoria=24, cpu_nome='i5 - 11400F', cpu_cores=11, cpu_clock=4.8, memoria_qntGB=16)
pc1.mostrar_Configuracao()