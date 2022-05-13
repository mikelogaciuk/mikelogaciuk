from dataclasses import dataclass, asdict
import json


@dataclass
class DataOpsEngineer:
    name: str
    role: str
    birth: int
    spoken_languages: list
    skills: list
    software: list

    def to_json(self):
        print(json.dumps((asdict(self)), indent=4))


me = DataOpsEngineer("Mike Logaciuk",
                     "DataOps Engineer",
                     1989,
                     ["pl_PL", "en_US"],
                     ["T-SQL", "PL/SQL", "Python", "Pandas", "Numpy", "ETL"],
                     ["SMSS", "SSIS", "VSCODE", "GRAFANA", "INTELLIJ IDEA", "PYCHARM", "DOCKER", "GITLAB", "CICD", "ERP", "POS"])

me.to_json()
