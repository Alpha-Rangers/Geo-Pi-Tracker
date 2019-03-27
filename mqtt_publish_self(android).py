from kivy.lang import Builder
from plyer import gps
from kivy.app import App
from kivy.properties import StringProperty
from kivy.clock import Clock, mainthread
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
import time

pnconfig = PNConfiguration()
pnconfig.publish_key = "pub-c-29e0c45e-724c-42ba-be7b-cb156fc74a03"
pnconfig.subscribe_key = "sub-c-f739ed7a-2afb-11e9-8c30-16f8bea0bbad"
pnconfig.ssl = False
pubnub = PubNub(pnconfig)
pubnub.publish().channel("Self_Loc").message("Initializing GPS sequence...").sync()
time.sleep(2)
pubnub.publish().channel("Self_Loc").message("Accessing Google Map Services...").sync()
time.sleep(2)
pubnub.publish().channel("Self_Loc").message("Determining the co-ordinates...").sync()
time.sleep(2)
pubnub.publish().channel("Self_Loc").message("Trangulating the location...").sync()
time.sleep(4)
pubnub.publish().channel("Self_Loc").message("Connected !").sync()

kv = '''
BoxLayout:
    orientation: 'vertical'

    Label:
        text: app.gps_location

    Label:
        text: app.gps_status

    BoxLayout:
        size_hint_y: None
        height: '48dp'
        padding: '4dp'

        ToggleButton:
            text: 'Start' if self.state == 'normal' else 'Stop'
            on_state:
                app.start(5000, 5) if self.state == 'down' else \
                app.stop()
'''


class GpsTest(App):

    gps_location = StringProperty()
    gps_status = StringProperty('Click Start to get GPS location updates')

    def build(self):
        try:
            gps.configure(on_location=self.on_location,
                          on_status=self.on_status)
        except NotImplementedError:
            import traceback
            traceback.print_exc()
            self.gps_status = 'GPS is not implemented for your platform'

        return Builder.load_string(kv)

    def start(self, minTime, minDistance):
        gps.start(minTime, minDistance)

    def stop(self):
        gps.stop()

    @mainthread
    def on_location(self, **kwargs):
        self.gps_location = '\n'.join([ '{}={}'.format(k, v) for k, v in kwargs.items()])   
        for k, v in kwargs.items():
        	print(k)
        	if k=="lat":
        		lat_variable = repr(v)
        	if k=="lon":
        		long_variable = repr(v)
        	
        pubnub.publish().channel("Self_Loc").message(lat_variable+"_"+long_variable).sync()
            		

    @mainthread
    def on_status(self, stype, status):
        self.gps_status = 'type={}\n{}'.format(stype, status)

    def on_pause(self):
        gps.stop()
        return True

    def on_resume(self):
        gps.start(5000, 5)
        pass


if __name__ == '__main__':
    GpsTest().run()
