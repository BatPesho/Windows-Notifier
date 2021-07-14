import winrt.windows.ui.notifications as notifications
import winrt.windows.data.xml.dom as dom
from threading import *
from beepy import beep
import datetime
from time import sleep
another_alarm = True

i = -1
do_you_want_another_alarm_loop_checker = True


def welcome():
    print("""                                                        
            ..:::..           
         .::::...::i:.        
        ::           :.       
     .  :                     
      JjBQBR: .r7 rgQgZ7r     
    vBBBBBBQi  i. dBBBBBBP.   
   BBBBPqii7PBBBBD1vLPBBBBBs  
   BQ: :QBBD2vir72dQBBL.iQBg  
      BQs.    :.    .rBQ:     
    KBJ   .r  ::  .i   7BB    
   PB: .   .  i:      :..BB   
  .B7  v7i:. .7i   .ivY  .B5  
  BB .    :qPi  .rKU:   . MB  
  Qg :r.    .vBBYi     :: vB. 
  BB ..       i7        . UB  
  XB   ..             : . BB  
   BB .r:             i. UB.  
   .BB    .i   .   :. ..5Br   
    .BBr  ..  ii   .: rBBi    
      LBQZr..  . ..rSBB2      
        rZBBBQBBBBBBB7.       
             ....                    
    """)


class AlarmClock(Thread):
    def run(self):
        thread_date = date1
        thread_info = info
        thread_optional_info = optional_info
        have_both_dates_overlapped = True
        while have_both_dates_overlapped:
            todey = datetime.datetime.now().replace(microsecond=0)
            if thread_date == todey:
                #print("Dates are the same. End")
                app = '{1AC14E77-02E7-4E5D-B744-2EB1AE5198B7}\\WindowsPowerShell\\v1.0\\powershell.exe'

                # create notifier
                nManager = notifications.ToastNotificationManager
                notifier = nManager.create_toast_notifier(app)

                # define notification as string
                tString = """
                  <toast>
                    <visual>
                      <binding template='ToastGeneric'>
                        <text>{}</text>
                        <text>{}</text>
                      </binding>
                    </visual>
                    <actions>
                      <action
                        content="Delete"
                        arguments="action=delete"/>
                      <action
                        content="Dismiss"
                        arguments="action=dismiss"/>
                    </actions>        
                  </toast>
                """
                tString = tString.format(thread_info, thread_optional_info)
                # convert notification to an XmlDocument
                xDoc = dom.XmlDocument()
                xDoc.load_xml(tString)

                # display notification
                beep(sound='plink')
                notifier.show(notifications.ToastNotification(xDoc))
                have_both_dates_overlapped = False
            else:
                sleep(0.100)


while another_alarm:
    welcome()
    i += 1
    th = "th"
    the_i = str(i)
    th = th + the_i
    th = AlarmClock()
    print(th)
    global today
    is_date_alright = True
    while is_date_alright:
        try:
            date_entry = input('Enter a date in YYYY-MM-DD-HH-mm format:')
            today = datetime.datetime.now().replace(microsecond=0)
            year, month, day, hours, minutes = map(int, date_entry.split('-'))
            date1 = datetime.datetime(year, month, day, hours, minutes)

            info = input("Enter a title caption for your event:")
            optional_info = input("Optional description. Enter None if you have no need for one:")
            if date1 < today:
                print("You cannot time travel.")
                continue
            #print(date1)
            is_date_alright = False
           #the exiled block goes here
        except(ValueError, OverflowError):
            print("Please add valid date input.")
    th.start()

    """ exiled block
while do_you_want_another_alarm_loop_checker:
    question = input("Do you want another alarm clock?[y/n]")
    if question == "y" or question == "Y":
        another_alarm = True
        break
    elif question == "n" or question == "N":
        another_alarm = False
        do_you_want_another_alarm_loop_checker = False
    else:
        print("Please enter a valid argument")
        continue
    """