![mikelogaciuk](./img/homescreen.png)

# Hi there 👋

```py
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
```

## About me

I am DataOps Engineer from :poland: workin at [TERG S.A. (MediaExpert)](https://mediaexpert.pl).

I am currently working on Python & SQL :heartpulse: projects.

Since my job is to obtain and move or wrangle specific sales data between POS & ERP systems, altogether with many integrity reports and because of my `NDA` - It's hard for me to share my code as others.

However I plan to cover it up with some things in future :smile:!

## Stats

[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=mikelogaciuk&layout=compact)](https://github.com/anuraghazra/github-readme-stats)
