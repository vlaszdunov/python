class Dockerfile:

    data = []

    def __init__(self) -> None:
        pass

    def instruction_from(self, parrent_source: str = 'scratch') -> None:
        self.data.append(f'FROM {parrent_source}')
    
    def instruction_workdir(self,workdir):
        self.data.append(f'WORKDIR {workdir}')
    
    def instruction_copy(self,copy_source):
        self.data.append(f'COPY {copy_source}')
    
    def instruction_add(self,add):
        self.data.append(f'ADD {add}')
    
    def instruction_run(self,run_command):
        self.data.append(f'RUN {run_command}')
    
    def instruction_cmd(self,cmd_command):
        self.data.append(f'CMD {cmd_command}')
    
    def add_space(self):
        self.data.append('')
    
    def instruction_comment(self,comment):
        self.data.append(f'# {comment}')
    
    def save_dockerfile(self):
        dockerfile=open('Dockerfile','w',encoding='UTF-8')
        for line in self.data:
            dockerfile.write(f'{line} \n')
        dockerfile.close()