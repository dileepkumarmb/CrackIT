*** Settings ***
#Documentation    Suite description
Library     RequestsLibrary
Library     Collections
Library     Logging

*** Variables ***
${base_url}=    http://restapi.demoqa.com/customer

*** Test Cases ***
Put_CustomerRegistration
    create session   mysession    ${base_url}
    ${body}=  create dictionary     FirstName=ameoba1243      LastName=Kumar      UserName=ameoba1243         Password=abc@123    Email=ameoba1243@gmail.com
    ${header}=  create dictionary      Content-Type=application/json
    ${response}=     post request     mysession   /register    data=${body}       headers=${header}

    log to console       ${response.status_code}
    log to console      ${response.content}

    #VALIDATIONS
    ${response_body}=   convert to string   ${response.content}
    should contain      ${response_body}     OPERATION_SUCCESS
    should contain      ${response_body}     Operation completed successfully
    ${res_code}=   convert to string     ${response.status_code}
    should be equal      ${res_code}      201