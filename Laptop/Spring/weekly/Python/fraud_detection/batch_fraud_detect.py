import pandas as pd
df = pd.read_csv("C:/Users/anuryadav/Desktop/Deskpot/FI/FilteredData.csv");
data = df.values
no_of_rows, no_of_col = data.shape

i=0

for row in data:
    flag = False 
   # print("Needs Validation ",data.item((i,0)), data.item((i+1,0)))
    if data.item((i,0)) == data.item((i+1,0)):        
        #print("flag as error", data.item((i,1)), data.item((i+1,1)))
        if data.item((i,3)) != data.item((i+1,3)):
          #  print("flag as error col 3 RULE_TOT_INC_AMT row no",i, "data:", data.item((i,3)), data.item((i+1,3)))
            flag = True
        if data.item((i,4)) != data.item((i+1,4)):
           # print("flag as error col 4 RULE_AID_REQUEST_SW ",i, "data:", data.item((i,4)), data.item((i+1,4)))
            flag = True
        if data.item((i,5)) != data.item((i+1,5)):
            #print("flag as error col 3 RULE_ACTIVE_IN_CASE_SW ",i, "data:", data.item((i,5)), data.item((i+1,5)))
            flag = True
        if data.item((i,6)) != data.item((i+1,6)):
            #print("flag as error col 4 US_CITIZEN_SW ",i, "data:", data.item((i,6)), data.item((i+1,6)))
            flag = True
        if data.item((i,7)) != data.item((i+1,7)):
            #print("flag as error col 3 RULE_RESIDENCY_STATE_CD ",i, "data:", data.item((i,7)), data.item((i+1,7)))
            flag = True
        if data.item((i,8)) != data.item((i+1,8)):
            #print("flag as error col 4 PROG_CD ",i, "data:", data.item((i,8)), data.item((i+1,8)))
            flag = True

    if(flag == True):
        print("Error in row no: ",i)
    i=i+1
    
    if i == no_of_rows - 1:
        break
    