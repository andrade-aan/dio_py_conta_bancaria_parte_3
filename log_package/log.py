
# abstração - Estrutura de Padrão de Projeto Template Method
from abc import ABC, abstractmethod
from pathlib import Path
import datetime as dt

LOG_FILE = Path(__file__).parent / 'log.txt' # criar o caminho do arquivo log.txt

print("CAMINHO = ",LOG_FILE)

class Log(ABC):
        
    # def log(self, msg): É a assinatura do método
    @abstractmethod
    def _log(self, msg): # vai receber uma mensagem como argumento
        ...# raise NotImplementedError('Implemente o método log')
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}') # aqui, o self.log representará cada filha de Log
        
    def log_success(self,msg):
        return self._log(f'Success: {msg}')
    
class LogFileMixin(Log):
    
    def _log(self, msg): # A classe que herda deve, por princípio, ter a mesma assinatura 
        log_instate = dt.datetime.now()
        reg_data_hora = log_instate.strftime("%d-%m-%Y %H:%M:%S")
        msg_formatada = f'{reg_data_hora} - {msg} :{self.__class__.__name__} -  - {log_instate}'
        print(msg_formatada)
        if not LOG_FILE.exists():
            with open(LOG_FILE, 'w') as arquivo:
                arquivo.write(msg_formatada)
                arquivo.write('\n')
                arquivo.close()
        else:
            with open(LOG_FILE, 'a') as arquivo:
                arquivo.write(msg_formatada)
                arquivo.write('\n')
                arquivo.close()
        
class LogPrintMixin(Log):
    def _log(self, msg): # seguindo o processo de mesma assinatura
        print(f'{msg} :{self.__class__.__name__}')
        
        log_instante = dt.datetime.now()
        reg_data_hora = log_instante.strftime("%d-%m-%Y %H:%M:%S")
        msg_formatada = f'{reg_data_hora} - {msg} :{self.__class__.__name__} -  - {log_instante}'
        print(msg_formatada)
        if not LOG_FILE.exists():
            with open(LOG_FILE, 'w') as arquivo:
                arquivo.write(msg_formatada)
                arquivo.write('\n')
                arquivo.close()
        else:
            with open(LOG_FILE, 'a') as arquivo:
                arquivo.write(msg_formatada)
                arquivo.write('\n')
                arquivo.close()
        
if __name__ == '__main__':
    file_log = LogFileMixin()
    print_log = LogPrintMixin()
    print_log.log_error('Log de Printing ')
    file_log.log_success('Log de File Loaded ')
