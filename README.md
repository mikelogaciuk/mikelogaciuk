<!--![mikelogaciuk](./img/homescreen.png)-->

<p align="center">
  <a href="https://github.com/mikelogaciuk">
    <img width="1000" src="https://github.com/mikelogaciuk/mikelogaciuk/raw/main/img/homescreen.png" alt="logo" />
  </a>
</p>

# Hi there 👋

```py
@task
def call_api(url):
    response = requests.get(url)
    print(response.status_code)
    return response.json()


@flow
def api_flow(url):
    fact_json = call_api(url)
    return fact_json


print(api_flow("https://catfact.ninja/fact"))
```

## About me

I am DataOps Engineer from :poland: Poland working for [TERG S.A. (MediaExpert)](https://mediaexpert.pl) as a Senior SQL Server Applications Administrator, where I am responsible for various data analysis and engineering in sales  data related area.

## Stats

[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=mikelogaciuk&layout=compact)](https://github.com/anuraghazra/github-readme-stats)
