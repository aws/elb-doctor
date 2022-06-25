row_format ="{:>50}" * 3

dict = {'Id': 'i-02b8769a50bc64b1a', 'Port': 443}

print(row_format.format('TargetID','Health','Deatils'))
print(row_format.format(dict['Id'],dict['Port'],'Target.ResponseCodeMismatch'))




