import pandas as pd

# Import list of property locations
prop_title = pd.read_csv("data_4_c.csv")
df_locations = pd.DataFrame(prop_title)
state_file = list(df_locations["State"])
district_file = list(df_locations["District"])
area_file = list(df_locations["Area"])
url_file = list(df_locations["Link"])

house=[]
x=1
for a,b,c,d in zip(state_file,district_file,area_file,url_file):
 
    house_all={
        "State":a,
        "District":b,
        "Area":c,
        "Agent Name":d,
        
    }
    if house_all["Area"]=="Pulau Tikus":
        house.append(house_all)
       
    x+=1
    df = pd.DataFrame(house)
    df.to_csv('answer_4_c.csv',
            index=False, encoding='utf-8')
    