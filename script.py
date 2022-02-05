# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def update_damages():
    ret=[];
    for i in range(len(damages)):
        dmg=damages[i];
        toAppend=dmg;#default appending value to a returned list        
        modifier=dmg[-1];#here we are expecting to have B or M or d (for the string "Damages not recorded")
        premodifier=dmg[:-1];#expecting to find here a float a string (for the case "Damages not recorded")
        if(premodifier.replace('.','',1).isdigit()):  
            #checking that we've found a float, credits to https://www.geeksforgeeks.org/python-check-for-float-string/            
            multiplier="";
            if(modifier == "M"):
                #Millions modifier
                multiplier=1E6;                
            elif(modifier == "B"):   
                #Billions modifier   
                multiplier=1E9;                
            if(multiplier != ""):
                toAppend=int(float(premodifier)*multiplier);
        ret.append(toAppend);
    return ret;
    


# write your construct hurricane dictionary function here:
def construct_hurricane(damages):

    #damages is a list returned by update_damages function
    ret={};#we are returning a dictionary which values are another dictionaries
    keys=names; #these are keys of a first level of the returning dictionaries
    values={
            #every key of this dictionary becomes returning dictionary's innerKey
            #dictionary key. The values of this dictionary are lists which have
            #length equel to len(names).             
            "Name":names, "Month":months, "Year":years, 
            "Max sustained wind":max_sustained_winds, 
            "Areas affected":areas_affected, 
            "Deaths":deaths,
            "Damage":damages
        };
             
    for i in range(len(names)):#in this loop we are building returning dictionary
        outerKey=names[i];#this is the first level key of the returning dictionary
        ret[outerKey]={};
        for innerKey in values.keys():
            value=values[innerKey][i];#we can use indexing because every list has the same length            
            ret[outerKey][innerKey]=value;    
    return ret;






# write your construct hurricane by year dictionary function here:
def construct_hurricane_by_year(hurricanes):
    #huricanes is a dictionary returned by construct_hurricane() function
    ret={};
    for key in hurricanes.keys():
        year=hurricanes[key]["Year"];
        if(year not in ret):
            ret[year]=[];#there could be more then 1 hurricane in one year, so we need a list for each year
        ret[year].append(hurricanes[key]);
    return ret;






# write your count affected areas function here:
def get_affected_areas():
    #list areas_affected contains other lists, though we need to 
    #have two loops to traverse each element
    ret={};
    for i in range(len(areas_affected)):        
        areas=areas_affected[i];#inner lists inside areas_affected list
        for area in areas:#every area inside the inner list
            if(area not in ret):#counting how many times we've found every area
                ret[area]=1;
            else:
                ret[area]+=1;        
    return ret;





# write your find most affected area function here:
def get_most_affected_area(affectedAreas):

    #expected affectedAreas be a returned dictionaty of get_affected_areas
    #function
    mostAffectedArea="";
    mostTimesHit=0;
    
    for (area,count) in affectedAreas.items():
        if(count > mostTimesHit):
            mostTimesHit=count;
            mostAffectedArea=area;
    
    return (mostAffectedArea,mostTimesHit);





# write your greatest number of deaths function here:
def get_greatest_number_of_deaths():

    data=zip(names,deaths);
    greatestName="";#the name of the hurricane that caused greatest numbe of deaths
    greatestToll=0;#greatest number of death caused by a hurricane
    
    for(name,toll) in data:
        if(toll > greatestToll):
            greatestToll=toll;
            greatestName=name;
            
    return (greatestName,greatestToll);



#give a hurricane a rating based of number of deathes it caused
def get_hurricane_mortality_rating(num_deaths):
    
    ret=0;
    if(num_deaths > 0 and num_deaths <= 100):
        ret=1;
    elif(num_deaths > 100 and num_deaths <= 500):
        ret=2;
    elif(num_deaths > 500 and num_deaths <= 1000):
        ret=3;
    elif(num_deaths > 1000 and num_deaths <= 5000):
        ret=4;
    elif(num_deaths > 5000):
        ret=5;
    elif(num_deaths < 0):
        #should not reach this
        print("num_deaths is negive:{num}".format(num=num_deaths));
        
    return ret;
    
def get_hurricane_damage_rating(damage): 
    ret=0;
    if(str(damage).isnumeric()):
        #damage can be if form of a string "Damages not recorded". 
        #isnumeric only checks for numbers, not for dot (".") signs 
        #but its ok, because inside function update_damages we've 
        #converted damage to an integer value so not dots should be present
        if(damage > 0 and damage <= 100000000):
            ret=1;
        elif(damage > 100000000 and damage <= 1000000000):
            ret=2;
        elif(damage > 1000000000 and damage <= 10000000000):
            ret=3;
        elif(damage > 10000000000 and damage <= 50000000000):
            ret=4;
        elif(damage > 50000000000):
            ret=5;
        elif(damage < 0):
            #should not reach this
            print("damage is negive:{num}".format(num=damage));
    else:
        #if damage presented by string Damages not recorded then we return just this string
        ret=damage;
    return ret;
        
        


# write your catgeorize by mortality function here:
def get_hurricanes_categorized_by_deathes(hurricanes):    
    #huricanes is a dictionary returned by construct_hurricane() function
    ret={};
    for key in hurricanes.keys():
        rating=get_hurricane_mortality_rating(hurricanes[key]["Deaths"]);
        if(rating not in ret):
            ret[rating]=[];#there could be several huricanes having same rating so we need a list to account them all
        ret[rating].append(hurricanes[key]);        
    return ret;



# write your greatest damage function here:
def get_greatest_damage(huricanes):
    #huricanes is a dictionary returned by construct_hurricane() function
    greatestName="";
    greatestDamage=0;
    for key in hurricanes.keys():       
        damage=hurricanes[key]["Damage"];        
        if(str(damage).isnumeric() and int(damage) > greatestDamage): #some damage is stored as "Damages not recorded" string
            greatestName=key;
            greatestDamage=damage;
            
    return (greatestName,greatestDamage);


# write your catgeorize by damage function here:
def get_hurricanes_categorized_by_damage(hurricanes):    
    #huricanes is a dictionary returned by construct_hurricane() function
    ret={};
    for key in hurricanes.keys():
        rating=get_hurricane_damage_rating(hurricanes[key]["Damage"]);
        if(rating not in ret):
            ret[rating]=[];#there could be several huricanes having same rating so we need a list to account them all
        ret[rating].append(hurricanes[key]);        
    return ret;




updated_damages=update_damages();
hurricanes=construct_hurricane(updated_damages);
hurricanes_by_year=construct_hurricane_by_year(hurricanes);
affected_areas=get_affected_areas();
(mostAffectedArea,mostTimesHit)=get_most_affected_area(affected_areas);
(greatestDeathName,greatestToll)=get_greatest_number_of_deaths();
hurricanes_categorized_by_deathes=get_hurricanes_categorized_by_deathes(hurricanes);
(greatestDamageName,greatestDamage)=get_greatest_damage(hurricanes);
hurricanes_categorized_by_damage=get_hurricanes_categorized_by_damage(hurricanes);
#print(affected_areas);
#print("Area {area} is most affected by hurricanes. It was hit {times} times".format(area=mostAffectedArea,times=mostTimesHit));
#print(updated_damages);
#print(hurricanes);
#print("Greates number of death were caused by the hurricane {Name}; It caused {Number} deathes".format(Name=greatestDeathName,Number=greatestToll));
#print(hurricanes_categorized_by_deathes);
#print("Greates recorded damage was caused by the hurricane {Name}; Its damage was {Damage} dollars".format(Name=greatestDamageName,Damage=greatestDamage));
#print(hurricanes_categorized_by_damage);


