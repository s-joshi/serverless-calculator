**Serverless calculator application**

This is is a serverless calculator application deployed on AWS using serverless framework and AWS Lambda.

**Please follow the following links and procedures to use the API:**

URL: `https://pcdqjj6je1.execute-api.us-east-1.amazonaws.com/dev/calc`

Parameters:
`operand_1` -- This is first operand of the API
`operand_2` -- This is second operand of the API
`operator`  -- This will be operator which can be applied on the operands.

Please use the operators as follows:

for `+` use `add`

for `-` use `minus`

for `/` use `div`

for `*` use `mult`

for `%` use `mod`

**Sample request without error**
https://pcdqjj6je1.execute-api.us-east-1.amazonaws.com/dev/calc?operand_1=2&operand_2=5&operator=add

**Sample Response without error**
`{
    "operand_1": "2",
    "operand_2": "5",
    "operator": "+",
    "result": 7,
    "status_code": 200
}`

**Sample request with error**
https://pcdqjj6je1.execute-api.us-east-1.amazonaws.com/dev/calc?operand_1=2&operand_2=5&operator=+

**Sample Response with error**
`{
    "error": "invalid parameters",
    "operand_1": "2",
    "operand_2": "5",
    "operator": " ",
    "status_code": 400
}`
