student_data={"id1":
{"name":["sara"],
"class":["V"],
 "subject_integration":["english,maths,science"]

},

"id2":
{"name":["Ali"],
"class":["V"],
 "subject_integration":["english,maths,science"]

},


"id3":
{"name":["sara"],
"class":["V"],
 "subject_integration":["english,maths,science"]
},


"id4":
{"name":["Zarrar"],
"class":["V"],
 "subject_integration":["english,maths,science"]
},
}

result={}

for key,value in student_data.items():
 if value not in result.values():
  result[key]=value
print(result)








