'''
Created on Sep 26, 2016

@author: Karim Hammouda

@copyright: Karim Hammouda

@version: version 2.0

@summary: JSON Inquiry script to traverse JSON formated input string json_data 
          returning corresponding key_value to inquired key (should be only one occurrence)
         
'''

''' 
importing libraries
'''

#import sys
import json

'''
define main module
'''

def walkJSONobj(dic, key):
    #convert dictionary object into corresponding list of items
    dic_stack = list(dic.items())
    #loop to search for subject key within stack representation of dictionary items.
    while dic_stack:
        #pick one [key,value] pair each time
        k,v = dic_stack.pop()
        #check if key is equal to subject key
        if k == key:
            #return corresponding value
            return v
        else:
            #check if value is nested dictionary
            if isinstance(v, dict):
                #append the nested dictionary to searching stack
                dic_stack.extend(v.items())
        
def main():
    '''
    @param argv[1]: JSON formatted input string
    @param argv[2]: JSON key inquiry
    '''
    #json_data = str(sys.argv[1])
    #key = str(sys.argv[2])
    json_data = '{"key2": {"key2_1": {"key2_1_1": "val2_1_1"}, "key2_2": "val2_2"}, "key3": "val3"}'
    key = 'key2_1'
    '''
    Checking if no input data then do nothing.
    '''
    if json_data is not None:
        '''
        Check if input string cannot be loaded into a JSON format
        '''
        try:
            '''
            load PYTHON native dictionary object corresponding to 
            JSON formatted input string 
            '''
            parsed_json = json.loads(json_data)
        except ValueError as error:
            '''
            Catch conversion error wrapping its details 
            notifying the user in order to fix if applicable
            '''
            print ("Oops!  malformed JSON structure... \n" + '(' + error.msg + ')')
            '''
            Terminate script
            '''
            return
        '''
        Check if no key path inquiry
        '''
        if key is not None:
            #walk nested JSON object and return corresponding value
            #if there is match with subject key 
            key_value = walkJSONobj(parsed_json, key)
            #print string representation of JSON value
            print(str(key_value))
'''
conditionally executing code in a module main when it is run as a script
'''
if __name__ == "__main__":
    main()
