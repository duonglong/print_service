JFW Script File                                                           P  (     jawsscriptsfromfoxitasazbemxn           isfilepagesubmenu        getfocus    '      %     getwindowclass    ListBox 
        %     getparent   '  %        %    getparent   '  %        %    getwindowclass    FoxitRibbonBackstageView    
             	                        	      H    isfilepagelistbox        getfocus    '      %     getwindowclass    ListBox 
          '  %       
        %     getparent   '   %                 	      %       
  '   l       %     getwindowclass    FoxitRibbonBackstageView    
             	                  	      l    isfilepagesubdialog      getfocus    '      %     getwindowclass  '  %    Button  
  " � %    Edit    
  
          '  %       
        %     getparent   '   %                 	      %       
  '   �       %     getwindowclass    FoxitRibbonBackstageView    
             	                  	      �     isfilepagemainmenu       getfocus    '      %     getwindowclass    FoxitRibbonBackstageView    
  # �      getobjecttypecode        
  
             	               	      d    isstartpagewindow        getfocus    '              getfocusobject  '     %            accvalue      stringlower '     %     getwindowclass    Internet Explorer_Server    
  #     %    startpage     stringcontains  
  # 4   %    index.html    stringcontains  
             	               	         �     isinribbonmenu       getfocus    '      %     getwindowclass  '     %    BCGPRibbonBar     stringcontains             	               	         l    isstartpageusenowlink       %    /   
              	           getfocus    '             getfocusobject  '     %            accvalue      stringlower '     %    getwindowclass    Internet Explorer_Server    
  # <   %    javascript:void(0)    stringcontains  
             	               	         �     saystartpageusenowlink                getfocusobject  '  %            accname '       /   %     indicatecontroltype       %         say       �    saytutorialhelp          getfocus    '     %    getwindowclass    MDIClient   
     	           isfilepagesubmenu   " �      isinribbonmenu  %     N   
  " � %        
  
  
  
           %   %    saytutorialhelp          %    gettutorialhelpoutputtype   '       isfilepagesubmenu           Message 1  To navigate among Backstage View tabs, use the Up or Down ARROW keys. To open the current one, press ENTER. %    sayusingvoice              isfilepagemainmenu          Message 1  To interact with current item press Enter.  %    sayusingvoice         %     N   
       isinribbonmenu  
          Message 1  Press Alt + Down Arrow for more options.    %    sayusingvoice           gethotkey   '     %    expandaltcommainhotkey        %    stringisblank             Message %         sayusingvoice               d    getribbonstatus   � �       getfocus    '     %    getwindowclass  '     %    BCGPRibbonBar     stringcontains                getfocusobject  '       getobjecttypecode   '       getobjectname   '  %       
          '      %       
           '           '                  '         �    activeitemchangedevent               isfilepagesubmenu           sayfocusedobject                  gettutorialhelpoutputtype   '       Message 1  To navigate among Backstage View tabs, use the Up or Down ARROW keys. To open the current one, press ENTER. %    sayusingvoice      	         %   %  %  %  %  %    activeitemchangedevent        \     selectionchangedevent           %   %  %    selectionchangedevent         �    getfilepagesubdialogstatictext       getfocus    '      %     getpriorwindow  '  %  # �    %    getwindowsubtypecode         
  
        %    getpriorwindow  '   \    %          %     getfirstwindow  '        %    getnextwindow   '     %  '   %   # \   %     getwindowsubtypecode         
  
        %                 getwindowtextex '     %    stringisblank        %    
   
  %  
  '        %     getnextwindow   '                   getfocusobject  '  %            accname '     %    stringisblank           %    stringlength    '     %    stringlength    '     %  %    stringright '     %  %    stringcompare         
     %  %  
        %  %       
    stringright '     %         stringleft  '  %    
   
     %     	            %  %    stringchopright '        %     	      �    sayfilepagelistbox                getfocusobject  '        '        '       getfocus    '       getfilepagesubdialogstatictext  '     %    stringisblank           %         say             %    getwindowname     saystring              '  %  %      accchildcount   
     %    %    accstate          
     %    %    accstate         
     %  '     %       
  '     %       
  '   $   %        
     %           accstate          
       %           accname '     %    saystring                  %    getwindowtype     saystring         %          say    %        
             1 cmsgPosInGroup2%1 items 1 cmsgPosInGroup2%1 items %    sayformattedmessage               1 cmsgPosInGroup1%1 of %2 1 cmsgPosInGroup1%1 of %2 %       
  %    sayformattedmessage              sayobjecttypeandtext           %   %    wassayobjecttypeandtextexceptionprocessed      	              %     getobjectname   '          %     getobjectsubtypecode    '       isfilepagesubmenu         %         say    %             1
 cmsgSilent    indicatecontroltype       	           isfilepagemainmenu             isfilepagelistbox         %    sayfilepagelistbox     	           isfilepagesubdialog         getfilepagesubdialogstatictext  '     %    stringisblank           %         say          %   %    sayobjecttypeandtext       	         %  %    isstartpageusenowlink         %    saystartpageusenowlink     	         %   %    sayobjecttypeandtext          �     shouldsayallondocumentload       isstartpagewindow               	           shouldsayallondocumentload     	          handlecustomwindows               getfocusobject  '     %     getwindowclass    MDIClient   
             	           isstartpagewindow              %            accname   saymessage              	               	           $saypagenumber     