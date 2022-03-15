#!/bin/bash

cd ../src

#./test_random.py $1 100000 100 5000 uniform iso_dd                           SSPM
#./test_random.py $1 100000 100 5000 uniform polynomial                       SSPM
#./test_random.py $1 100000 100 5000 uniform sbx                              SSPM
#./test_random.py $1 100000 100 5000 uniform polynomial+sbx                   SSPM
#./test_random.py $1 100000 100 5000 uniform iso_dd+polynomial                SSPM
#./test_random.py $1 100000 100 5000 uniform iso_dd+sbx                       SSPM
#./test_random.py $1 100000 100 5000 uniform iso_dd+polynomial+sbx            SSPM

./test_random.py $1 200000 100 5000 curiosity curiosity_func                      	
./test_random.py $1 200000 100 5000 curiosity iso_dd                        	
./test_random.py $1 200000 100 5000 curiosity polynomial                     
./test_random.py $1 200000 100 5000 curiosity sbx                            
./test_random.py $1 200000 100 5000 curiosity polynomial+sbx                 
./test_random.py $1 200000 100 5000 curiosity iso_dd+polynomial              
./test_random.py $1 200000 100 5000 curiosity iso_dd+sbx                     
./test_random.py $1 200000 100 5000 curiosity iso_dd+polynomial+sbx          

./test_random.py $1 200000 100 5000 uniform iso_dd                        	
./test_random.py $1 200000 100 5000 uniform polynomial                     
./test_random.py $1 200000 100 5000 uniform sbx                            
./test_random.py $1 200000 100 5000 uniform polynomial+sbx                 
./test_random.py $1 200000 100 5000 uniform iso_dd+polynomial              
./test_random.py $1 200000 100 5000 uniform iso_dd+sbx                     
./test_random.py $1 200000 100 5000 uniform iso_dd+polynomial+sbx          

./test_random.py $1 200000 100 5000 curiosity-child iso_dd                   
./test_random.py $1 200000 100 5000 curiosity-child polynomial               
./test_random.py $1 200000 100 5000 curiosity-child sbx                      
./test_random.py $1 200000 100 5000 curiosity-child polynomial+sbx           
./test_random.py $1 200000 100 5000 curiosity-child iso_dd+polynomial        
./test_random.py $1 200000 100 5000 curiosity-child iso_dd+sbx               
./test_random.py $1 200000 100 5000 curiosity-child iso_dd+polynomial+sbx    
                                                                     
#./test_random.py $1 100000 100 5000 uniform polynomial momentum              SSPM
#./test_random.py $1 100000 100 5000 uniform polynomial+sbx momentum          SSPM
#./test_random.py $1 100000 100 5000 uniform iso_dd+polynomial momentum       SSPM
#./test_random.py $1 100000 100 5000 uniform iso_dd+polynomial+sbx momentum   SSPM
#./test_random.py $1 100000 100 5000 curiosity polynomial momentum            SSPM
#./test_random.py $1 100000 100 5000 curiosity polynomial+sbx momentum        SSPM
#./test_random.py $1 100000 100 5000 curiosity iso_dd+polynomial momentum     SSPM
#./test_random.py $1 100000 100 5000 curiosity iso_dd+polynomial+sbx momentum SSPM
