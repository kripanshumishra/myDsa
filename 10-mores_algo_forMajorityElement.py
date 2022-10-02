# arr=[1,2,1,2,1,3,3,3]
# def Mories (arr):
#     elem1=arr[0]
#     freq1=1
#     elem2=None
#     freq2=0
#     for i in range(1,len(arr)):
#         if( arr[i] == elem1 ):
#             freq1+=1
#         elif( arr[i] == elem2 ):
#             freq2+=1
#         else:
#             if( freq1==0 ):
#                 elem1=arr[i]
#                 freq1=1
#             elif( freq2==0 ):
#                 elem2=arr[i]
#                 freq2=1
#             else:
#                 freq1-=1
#                 freq2-=1
#             if( freq1==0 ):
#                 elem1=None
#             if( freq2==0 ):
#                 elem2=None
#     return [elem1,elem2]
# Mories(arr)

dic= { 'name':'kripanshu','class':5 }
print(dic)
for i in dic:
    print(i)