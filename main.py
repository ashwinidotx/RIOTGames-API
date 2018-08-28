from RiotSumm import RiotSumm

def main():
    api=RiotSumm('RGAPI-3b0be3d6-1f3c-4e6f-9e52-9d9904af2c21')
    r=api.get_summoner_by_name('shadyjoker27')
    print (r)

if __name__=="__main__":
    main()