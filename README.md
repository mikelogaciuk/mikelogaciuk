<!--![mikelogaciuk](./img/homescreen.png)-->

<p align="center">
  <a href="https://github.com/mikelogaciuk">
    <img width="1000" src="https://github.com/mikelogaciuk/mikelogaciuk/raw/main/img/homescreen.png" alt="logo" />
  </a>
</p>

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
                     ["T-SQL", "PL/SQL", "PYTHON",
                     "PANDAS", "ETL", "ELT", "ERP", "POS"],
                     ["SMSS", "VSCODE", "PYCHARM", "DOCKER",
                     "GITLAB", "CICD", "GRAFANA", "SPLUNK"])

me.to_json()
```

## About me

I am DataOps Engineer from :poland: Poland working for [TERG S.A. (MediaExpert)](https://mediaexpert.pl) as a Senior SQL Server Applications Administrator.

My job there is to write various integrity checks around our sales data, wrangle it or analyse for internal purposes.

Another part of my job is to create various dashboards, alerts or healthchecks.

Unfortunately, since almost everything that I write is used for internal purposes and because of my **NDA** - it's quite complicated to share the code publicly.

However I plan to cover it up with some custom things in future.

If I find a time :smile:!

## Stats

[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=mikelogaciuk&layout=compact)](https://github.com/anuraghazra/github-readme-stats)
