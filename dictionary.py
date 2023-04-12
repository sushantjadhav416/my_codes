stuinfo={
        "name":"sushant",
        "age":"20",
        "steam":"electronics",
        "marks":{"1st year":50,"2nd year":70,"3rd year":75}
}
stuinfo['marks']['1st year']=34
print(stuinfo)
print(stuinfo.keys())
print(stuinfo.values())
print(stuinfo.items())
update_record={
     "ID":2018088794
}
stuinfo.update(update_record)
print(stuinfo)





