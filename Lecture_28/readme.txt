http http://127.0.0.1:8000/studentapi/

http http://127.0.0.1:8000/studentapi/000/studentapi/ 'Authorization:Token c113376acdcb3a892c7b2878ac6359cd93651966'

http -f POST http://127.0.0.1:8000/studentapi/ name=Jay roll=104 city=Dhanbad 'Authorization:Token c113376acdcb3a892c7b2878ac6359cd93651966'

http PUT http://127.0.0.1:8000/studentapi/3/ name=Kunal roll=105 city=Durgapur 'Authorization:Token c113376acdcb3a892c7b2878ac6359cd93651966'

http DELETE http://127.0.0.1:8000/studentapi/3/ 'Authorization:Token c113376acdcb3a892c7b2878ac6359cd93651966'