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
                     ["T-SQL", "PL/SQL", "Python",
                     "Pandas", "Numpy", "ETL"],
                     ["SMSS", "SSIS", "VSCODE", "GRAFANA",
                     "INTELLIJ IDEA", "PYCHARM", "DOCKER",
                     "GITLAB", "CICD", "ERP", "POS"])

me.to_json()
```

## About me

I am DataOps Engineer from :poland: working at [TERG S.A. (MediaExpert)](https://mediaexpert.pl).

I usually write various integrity checks around our sales data, altogether with API's.
I am familiar with data modeling, wrangling, moving it out from one place into another.

:x: Since my job is to:

:asterisk: obtain and move or wrangle specific sales data between POS & ERP systems,
:asterisk: altogether with many integrity reports,
:asterisk: and because of my **NDA**.

:interrobang: It's hard for me to share internal code as others.

:hash: However I plan to cover it up with some custom things in future :smile:!

## Stats

[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=mikelogaciuk&layout=compact)](https://github.com/anuraghazra/github-readme-stats)
