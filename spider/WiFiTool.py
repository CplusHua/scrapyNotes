import re


########################################################################
class WifiTool:
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        pass
        
    
    
    
    #----------------------------------------------------------------------
    def parseBssidEssid(self,line):
        """"""
        print line
        
        
    def run(self):
        file_sql = open('newstock.sql','r+')
        try:
            lines = []
            lines = file_sql.readlines()
            
            for line in  lines:
                print line
                     
        finally:            
            file_sql.close()        
        #self.parseBssidEssid(line)
            

        
tool = WifiTool()
tool.run()