
# Currency Converter

This a small project to see currency live exchange values and the option to convert from one value to another using FIXER API


## API Reference

#### Get all items

```http
  url = "https://api.apilayer.com/fixer/latest?symbols={symbols}&base={base}"
  response = requests.request("GET", url, headers={api_key})
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `base` | `string` | **Optional** Three-letter currency code of your preferred base currency. |
| `symbols` | `string` | **Optional** List of comma-separated currency codes to limit output currencies. |


#### Get Coverted value

```http
  url = "https://api.apilayer.com/fixer/convert?to={to}&from={from}&amount={amount}"
  response = requests.request("GET", url, headers={api_key})
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `from`      | `string` | **Required**. Three-letter currency code of the currency you would like to convert from |
| `to`      | `string` | **Required**. Three-letter currency code of the currency you would like to convert to |
| `amount`      | `string` | **Required** The amount to be converted |



