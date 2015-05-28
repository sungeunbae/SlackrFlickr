import flickrapi
import pickle
PIK= "pickle.dat"

__author__ = 'seb56'




class PhotosWithLensInfo:
	def __init__(self, lens_tag, pids):
		self.lens_tag= lens_tag
		self.pids = pids

def get_taken_date(pid):
	#to get info
	"""
	<?xml version="1.0" encoding="utf-8" ?>
	<rsp stat="ok">
	  <photo id="17776324575" secret="eee1eea6a3" server="7678" farm="8" dateuploaded="1431872670" isfavorite="0" license="0" safety_level="0" rotation="0" originalsecret="9ef45c65a6" originalformat="jpg" views="22" media="photo">
	    <owner nsid="45867010@N02" username="sung.e.bae" realname="Sung Eun Bae" location="Christchurch, New Zealand" iconserver="5517" iconfarm="6" path_alias="sung_e_bae" />
	    <title>DSC05087</title>
	    <description />
	    <visibility ispublic="1" isfriend="0" isfamily="0" />
	    <dates posted="1431872670" taken="2015-05-17 16:25:47" takengranularity="0" takenunknown="0" lastupdate="1431898337" />
	    <permissions permcomment="3" permaddmeta="2" />
	    <editability cancomment="1" canaddmeta="1" />
	    <publiceditability cancomment="1" canaddmeta="0" />
	    <usage candownload="1" canblog="1" canprint="1" canshare="1" />
	    <comments>0</comments>
	    <notes />
	    <people haspeople="0" />
	    <tags />
	    <urls>
	      <url type="photopage">https://www.flickr.com/photos/sung_e_bae/17776324575/</url>
	    </urls>
	  </photo>
	</rsp>
	"""

	info = flickr.photos.getInfo(photo_id=pid)
	return info.find('photo').find('dates').get('taken')

def get_exifs(pid):
	"""
	<?xml version="1.0" encoding="utf-8" ?>
	<rsp stat="ok">
	  <photo id="17776324575" secret="eee1eea6a3" server="7678" farm="8" camera="Sony SLT-A55V">
	    <exif tagspace="IFD0" tagspaceid="0" tag="ImageDescription" label="Image Description">
	      <raw>SONY DSC                       </raw>
	    </exif>
	    <exif tagspace="IFD0" tagspaceid="0" tag="Make" label="Make">
	      <raw>SONY</raw>
	    </exif>
	    <exif tagspace="IFD0" tagspaceid="0" tag="Model" label="Model">
	      <raw>SLT-A55V</raw>
	    </exif>
	    <exif tagspace="IFD0" tagspaceid="0" tag="Orientation" label="Orientation">
	      <raw>Horizontal (normal)</raw>
	    </exif>
	    <exif tagspace="IFD0" tagspaceid="0" tag="XResolution" label="X-Resolution">
	      <raw>350</raw>
	      <clean>350 dpi</clean>
	    </exif>
	    <exif tagspace="IFD0" tagspaceid="0" tag="YResolution" label="Y-Resolution">
	      <raw>350</raw>
	      <clean>350 dpi</clean>
	    </exif>
	    <exif tagspace="IFD0" tagspaceid="0" tag="ResolutionUnit" label="Resolution Unit">
	      <raw>inches</raw>
	    </exif>
	    <exif tagspace="IFD0" tagspaceid="0" tag="Software" label="Software">
	      <raw>ACDSee Pro 8</raw>
	    </exif>
	    <exif tagspace="IFD0" tagspaceid="0" tag="ModifyDate" label="Date and Time (Modified)">
	      <raw>2015:05:17 20:52:15</raw>
	    </exif>
	    <exif tagspace="IFD0" tagspaceid="0" tag="YCbCrPositioning" label="YCbCr Positioning">
	      <raw>Centered</raw>
	    </exif>
	    <exif tagspace="ExifIFD" tagspaceid="0" tag="ExposureTime" label="Exposure">
	      <raw>1/125</raw>
	      <clean>0.008 sec (1/125)</clean>
	    </exif>
	    <exif tagspace="ExifIFD" tagspaceid="0" tag="FNumber" label="Aperture">
	      <raw>4.5</raw>
	      <clean>f/4.5</clean>
	    </exif>
	    <exif tagspace="ExifIFD" tagspaceid="0" tag="ExposureProgram" label="Exposure Program">
	      <raw>Program AE</raw>
	    </exif>
	    <exif tagspace="ExifIFD" tagspaceid="0" tag="ISO" label="ISO Speed">
	      <raw>250</raw>
	    </exif>
	    <exif tagspace="ExifIFD" tagspaceid="0" tag="SensitivityType" label="Sensitivity Type">
	      <raw>Recommended Exposure Index</raw>
	    </exif>
	    <exif tagspace="ExifIFD" tagspaceid="0" tag="RecommendedExposureIndex" label="Recommended Exposure Index">
	      <raw>250</raw>
	    </exif>
	    <exif tagspace="ExifIFD" tagspaceid="0" tag="ExifVersion" label="Exif Version">
	      <raw>0230</raw>
	    </exif>
	    <exif tagspace="ExifIFD" tagspaceid="0" tag="DateTimeOriginal" label="Date and Time (Original)">
	      <raw>2015:05:17 16:25:47</raw>
	    </exif>
	    <exif tagspace="ExifIFD" tagspaceid="0" tag="CreateDate" label="Date and Time (Digitized)">
	      <raw>2015:05:17 16:25:47</raw>
	    </exif>
	    <exif tagspace="ExifIFD" tagspaceid="0" tag="ComponentsConfiguration" label="Components Configuration">
	      <raw>Y, Cb, Cr, -</raw>
	    </exif>
	    <exif tagspace="ExifIFD" tagspaceid="0" tag="CompressedBitsPerPixel" label="Compressed Bits Per Pixel">
	      <raw>2</raw>
	    </exif>
	    <exif tagspace="ExifIFD" tagspaceid="0" tag="BrightnessValue" label="Brightness Value">
	      <raw>5.75</raw>
	    </exif>
	    <exif tagspace="ExifIFD" tagspaceid="0" tag="ExposureCompensation" label="Exposure Bias">
	      <raw>0</raw>
	      <clean>0 EV</clean>
	    </exif>
	    <exif tagspace="ExifIFD" tagspaceid="0" tag="MaxApertureValue" label="Max Aperture Value">
	      <raw>4.5</raw>
	    </exif>
	    <exif tagspace="ExifIFD" tagspaceid="0" tag="MeteringMode" label="Metering Mode">
	      <raw>Multi-segment</raw>
	    </exif>
	    <exif tagspace="ExifIFD" tagspaceid="0" tag="LightSource" label="Light Source">
	      <raw>Unknown</raw>
	    </exif>
	    <exif tagspace="ExifIFD" tagspaceid="0" tag="Flash" label="Flash">
	      <raw>Off, Did not fire</raw>
	    </exif>
	    <exif tagspace="ExifIFD" tagspaceid="0" tag="FocalLength" label="Focal Length">
	      <raw>70.0 mm</raw>
	      <clean>70 mm</clean>
	    </exif>
	    <exif tagspace="ExifIFD" tagspaceid="0" tag="SubSecTime" label="Sub Sec Time">
	      <raw>415</raw>
	    </exif>
	    <exif tagspace="ExifIFD" tagspaceid="0" tag="FlashpixVersion" label="Flashpix Version">
	      <raw>0100</raw>
	    </exif>
	    <exif tagspace="ExifIFD" tagspaceid="0" tag="ColorSpace" label="Color Space">
	      <raw>sRGB</raw>
	    </exif>
	    <exif tagspace="ExifIFD" tagspaceid="0" tag="FileSource" label="File Source">
	      <raw>Digital Camera</raw>
	    </exif>
	    <exif tagspace="ExifIFD" tagspaceid="0" tag="SceneType" label="Scene Type">
	      <raw>Directly photographed</raw>
	    </exif>
	    <exif tagspace="ExifIFD" tagspaceid="0" tag="CustomRendered" label="Custom Rendered">
	      <raw>Normal</raw>
	    </exif>
	    <exif tagspace="ExifIFD" tagspaceid="0" tag="ExposureMode" label="Exposure Mode">
	      <raw>Auto</raw>
	    </exif>
	    <exif tagspace="ExifIFD" tagspaceid="0" tag="WhiteBalance" label="White Balance">
	      <raw>Auto</raw>
	    </exif>
	    <exif tagspace="ExifIFD" tagspaceid="0" tag="FocalLengthIn35mmFormat" label="Focal Length (35mm format)">
	      <raw>105 mm</raw>
	    </exif>
	    <exif tagspace="ExifIFD" tagspaceid="0" tag="SceneCaptureType" label="Scene Capture Type">
	      <raw>Standard</raw>
	    </exif>
	    <exif tagspace="ExifIFD" tagspaceid="0" tag="Contrast" label="Contrast">
	      <raw>High</raw>
	    </exif>
	    <exif tagspace="ExifIFD" tagspaceid="0" tag="Saturation" label="Saturation">
	      <raw>Normal</raw>
	    </exif>
	    <exif tagspace="ExifIFD" tagspaceid="0" tag="Sharpness" label="Sharpness">
	      <raw>Hard</raw>
	    </exif>
	    <exif tagspace="ExifIFD" tagspaceid="0" tag="LensInfo" label="Lens Info">
	      <raw>16-80mm f/3.5-4.5</raw>
	    </exif>
	    <exif tagspace="ExifIFD" tagspaceid="0" tag="LensModel" label="Lens Model">
	      <raw>DT 16-80mm F3.5-4.5 ZA</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="LensSpec" label="Lens Spec">
	      <raw>Unknown (00 0 0 0 0 00)</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="FocalLengthTeleZoom" label="Focal Length Tele Zoom">
	      <raw>70.0 mm</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="FocusStatus" label="Focus Status">
	      <raw>AF-C - Confirmed</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="AFPointSelected" label="AFPoint Selected">
	      <raw>Auto</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="FocusMode" label="Focus Mode">
	      <raw>AF-C</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="AFPoint" label="AFPoint">
	      <raw>Lower-right</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="DriveMode2" label="Drive Mode2">
	      <raw>Continuous High</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="ExposureProgram" label="Exposure Program">
	      <raw>Program AE</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="MeteringMode" label="Metering Mode">
	      <raw>Multi-segment</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="DynamicRangeOptimizerSetting" label="Dynamic Range Optimizer Setting">
	      <raw>On (Manual)</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="DynamicRangeOptimizerLevel" label="Dynamic Range Optimizer Level">
	      <raw>3</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="ColorSpace" label="Color Space">
	      <raw>sRGB</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="CreativeStyleSetting" label="Creative Style Setting">
	      <raw>Vivid</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="ContrastSetting" label="Contrast Setting">
	      <raw>+1</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="SaturationSetting" label="Saturation Setting">
	      <raw>0</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="SharpnessSetting" label="Sharpness Setting">
	      <raw>+1</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="WhiteBalanceSetting" label="White Balance Setting">
	      <raw>Auto (0)</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="ColorTemperatureSetting" label="Color Temperature Setting">
	      <raw>5500 K</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="ColorCompensationFilterSet" label="Color Compensation Filter Set">
	      <raw>0</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="FlashMode" label="Flash Mode">
	      <raw>Flash Off</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="LongExposureNoiseReduction" label="Long Exposure Noise Reduction">
	      <raw>Off</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="HighISONoiseReduction" label="High ISONoise Reduction">
	      <raw>Auto</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="MultiFrameNoiseReduction" label="Multi Frame Noise Reduction">
	      <raw>Off</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="HDRSetting" label="HDRSetting">
	      <raw>Off</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="HDRLevel" label="HDRLevel">
	      <raw>3 EV</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="ViewingMode" label="Viewing Mode">
	      <raw>Quick AF Live View</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="FaceDetection" label="Face Detection">
	      <raw>On</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="CustomWB_RBLevels" label="Custom WB_ RBLevels">
	      <raw>535 581</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="ExposureCompensationSet" label="Exposure Compensation Set">
	      <raw>0</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="FlashExposureCompSet" label="Flash Exposure Comp Set">
	      <raw>0</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="LiveViewAFMethod" label="Live View AFMethod">
	      <raw>Phase-detect AF</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="FNumber" label="FNumber">
	      <raw>4.8</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="ExposureTime" label="Exposure Time">
	      <raw>1/128</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="FocalLength2" label="Focal Length2">
	      <raw>73.4 mm</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="ExposureCompensation2" label="Exposure Compensation2">
	      <raw>0</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="FlashExposureCompSet2" label="Flash Exposure Comp Set2">
	      <raw>0</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="Orientation2" label="Orientation2">
	      <raw>Horizontal (normal)</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="FlashAction2" label="Flash Action2">
	      <raw>Did not fire</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="FocusMode2" label="Focus Mode2">
	      <raw>AF</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="FacesDetected" label="Faces Detected">
	      <raw>1</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="Face1Position" label="Face1 Position">
	      <raw>1380 2730 750 750</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="TiffMeteringImage" label="Tiff Metering Image">
	      <raw>(Binary data 7404 bytes, use -b option to extract)</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="ImageCount" label="Image Count">
	      <raw>48471</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="ShutterCount" label="Shutter Count">
	      <raw>74637</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="ShotNumberSincePowerUp" label="Shot Number Since Power Up">
	      <raw>10</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="Quality" label="Quality">
	      <raw>Fine</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="FlashExposureComp" label="Flash Exposure Comp">
	      <raw>0</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="Teleconverter" label="Teleconverter">
	      <raw>None</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="WhiteBalanceFineTune" label="White Balance Fine Tune">
	      <raw>0</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="ShutterSpeedSetting" label="Shutter Speed Setting">
	      <raw>1/3158</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="ApertureSetting" label="Aperture Setting">
	      <raw>1.8</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="ISOSetting" label="ISOSetting">
	      <raw>Auto</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="DriveModeSetting" label="Drive Mode Setting">
	      <raw>Continuous High</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="FocusModeSetting" label="Focus Mode Setting">
	      <raw>AF-C</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="SonyImageSize" label="Sony Image Size">
	      <raw>Large (3:2)</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="AspectRatio" label="Aspect Ratio">
	      <raw>3:2</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="CustomWB_RGBLevels" label="Custom WB_ RGBLevels">
	      <raw>535 256 581</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="FlashControl" label="Flash Control">
	      <raw>Pre-flash TTL</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="AFAreaMode" label="AFArea Mode">
	      <raw>Wide</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="SmileShutterMode" label="Smile Shutter Mode">
	      <raw>Normal Smile</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="RedEyeReduction" label="Red Eye Reduction">
	      <raw>Off</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="SmileShutter" label="Smile Shutter">
	      <raw>Off</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="SweepPanoramaSize" label="Sweep Panorama Size">
	      <raw>Standard</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="SweepPanoramaDirection" label="Sweep Panorama Direction">
	      <raw>Right</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="DriveMode" label="Drive Mode">
	      <raw>Continuous High</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="LiveViewAFSetting" label="Live View AFSetting">
	      <raw>Phase-detect AF</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="PanoramaSize3D" label="Panorama Size3 D">
	      <raw>Standard</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="AFButtonPressed" label="AFButton Pressed">
	      <raw>No</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="LiveViewMetering" label="Live View Metering">
	      <raw>1200-zone Evaluative</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="ViewingMode2" label="Viewing Mode2">
	      <raw>Quick AF Live View</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="AELock" label="AELock">
	      <raw>Off</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="FlashAction" label="Flash Action">
	      <raw>Did not fire</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="LiveViewFocusMode" label="Live View Focus Mode">
	      <raw>AF</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="LensMount" label="Lens Mount">
	      <raw>A-Mount</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="SequenceNumber" label="Sequence Number">
	      <raw>Single</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="FolderNumber" label="Folder Number">
	      <raw>130</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="ImageNumber" label="Image Number">
	      <raw>5087</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="ShotNumberSincePowerUp2" label="Shot Number Since Power Up2">
	      <raw>10</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="WhiteBalance" label="White Balance">
	      <raw>Auto</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="BatteryTemperature" label="Battery Temperature">
	      <raw>28.3 C</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="BatteryLevel" label="Battery Level">
	      <raw>42%</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="BatteryVoltage1" label="Battery Voltage1">
	      <raw>6.43 V</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="BatteryVoltage2" label="Battery Voltage2">
	      <raw>6.39 V</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="ImageStabilization" label="Image Stabilization">
	      <raw>On</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="BatteryState" label="Battery State">
	      <raw>Low</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="CameraOrientation" label="Camera Orientation">
	      <raw>Rotate 270 CW</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="PreviewImage" label="Preview Image">
	      <raw>(Binary data 616295 bytes, use -b option to extract)</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="Rating" label="Rating">
	      <raw>0</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="Contrast" label="Contrast">
	      <raw>+1</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="Saturation" label="Saturation">
	      <raw>0</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="Sharpness" label="Sharpness">
	      <raw>+1</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="HDR" label="HDR">
	      <raw>Off; Uncorrected image</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="PictureEffect" label="Picture Effect">
	      <raw>Off</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="ColorTemperature" label="Color Temperature">
	      <raw>Auto</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="ColorCompensationFilter" label="Color Compensation Filter">
	      <raw>0</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="SceneMode" label="Scene Mode">
	      <raw>Standard</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="ZoneMatching" label="Zone Matching">
	      <raw>ISO Setting Used</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="DynamicRangeOptimizer" label="Dynamic Range Optimizer">
	      <raw>Lv3</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="LensType" label="Lens Type">
	      <raw>Carl Zeiss Vario-Sonnar T* DT 16-80mm F3.5-4.5 ZA (SAL1680Z)</raw>
	    </exif>
	    <exif tagspace="Sony" tagspaceid="0" tag="ColorMode" label="Color Mode">
	      <raw>Vivid</raw>
	    </exif>
	    <exif tagspace="InteropIFD" tagspaceid="0" tag="InteropIndex" label="Interop Index">
	      <raw>R98 - DCF basic file (sRGB)</raw>
	    </exif>
	    <exif tagspace="InteropIFD" tagspaceid="0" tag="InteropVersion" label="Interop Version">
	      <raw>0100</raw>
	    </exif>
	    <exif tagspace="IFD1" tagspaceid="0" tag="Compression" label="Compression">
	      <raw>JPEG (old-style)</raw>
	    </exif>
	    <exif tagspace="IFD1" tagspaceid="0" tag="ThumbnailOffset" label="Thumbnail Offset">
	      <raw>43578</raw>
	    </exif>
	    <exif tagspace="IFD1" tagspaceid="0" tag="ThumbnailLength" label="Thumbnail Length">
	      <raw>7813</raw>
	    </exif>
	    <exif tagspace="XMP-x" tagspaceid="0" tag="XMPToolkit" label="XMPToolkit">
	      <raw>XMP Core 5.1.2</raw>
	    </exif>
	  </photo>
	</rsp>
	"""
	exif=flickr.photos.getExif(photo_id=pid)
	exifs=exif.find('photo').findall('exif')
	return exifs

def get_exif_value(pid,tag):
	exifs=get_exifs(pid)
	for i in range(len(exifs)):
		if exifs[i].get('tag')== tag:
			return exifs[i].find('raw').text

	return None

def connect(auth_key, auth_secret, perms='write'):
	flickr = flickrapi.FlickrAPI(auth_key, auth_secret)
	flickr.authenticate_via_browser(perms='write')
	return flickr


auth_key="2c231aee6d8326a904306bee37737f78"
auth_secret = "1ddab017e73c8e13"

min_taken_date = "2014-01-01"
max_taken_date = "2015-05-21"

flickr = connect(auth_key, auth_secret)

userid = flickr.flickr_oauth.oauth_token.user_nsid

#public_photos = flickr.photos.search(user_id=userid, per_page='10', privacy_filter=1) #public photos
photos = flickr.photos.search(user_id=userid, per_page=100, min_taken_date=min_taken_date, max_taken_date=max_taken_date)


#https://www.flickr.com/services/api/explore/flickr.photos.search

"""
{ "photos": { "page": 1, "pages": 13, "perpage": 100, "total": "1281",
    "photo": [
      { "id": "17776324575", "owner": "45867010@N02", "secret": "eee1eea6a3", "server": "7678", "farm": 8, "title": "DSC05087", "ispublic": 1, "isfriend": 0, "isfamily": 0 },
      { "id": "17313718539", "owner": "45867010@N02", "secret": "69a5cbc458", "server": "8840", "farm": 9, "title": "DSC04941", "ispublic": 1, "isfriend": 0, "isfamily": 0 },
      { "id": "17289033972", "owner": "45867010@N02", "secret": "fae9a6245f", "server": "7716", "farm": 8, "title": "DSC04337", "ispublic": 1, "isfriend": 0, "isfamily": 0 },
      ....
      }
}
"""
total=photos.find('photos').get('total')
pages = photos.find('photos').get('pages')
perpage = photos.find('photos').get('perpage')

total = int(total)
pages=int(pages)
perpage = int(perpage)
print "Total :%d photos" %total

#maximum 500
for p in range(1,pages+1):

	photos = flickr.photos.search(user_id=userid, page=p, per_page=perpage, min_taken_date=min_taken_date, max_taken_date=max_taken_date)
	photos_elem =photos.find('photos')
	photo_elems = photos_elem.findall('photo')
	#public_photo_elems[0].keys()
	#['id', 'owner', 'secret', 'server', 'farm', 'title', 'ispublic', 'isfriend', 'isfamily']

	photo_ids=[]
	for i in range(len(photo_elems)):
		pid=photo_elems[i].get('id')
		photo_ids.append(pid)

	lens_models={}

	print "Page %d/%d " %(p,pages),
	print "%d photos will be processed" %len(photo_ids)
	non_lens=0
	total_photo_ids = len(photo_ids)
	for i in range(total_photo_ids):
		exif_text = None
		pid = photo_ids[i]
		try:
			exif_text=get_exif_value(pid,"LensModel")
		except flickrapi.exceptions.FlickrError:
			print "No handlers could be found for logger 'flickrapi.auth.OAuthFlickrInterface'"
			flickr = connect(auth_key, auth_secret)
			i=i-1
			total_photo_ids += 1
			continue

		if exif_text:
			lens_tag=exif_text.replace(' ','_')
			if lens_models.has_key(lens_tag):
				lens_models[lens_tag].append(pid)
			else:
				lens_models[lens_tag]=[pid]
		else:
			non_lens+=1
		# 'DT 16-80mm F3.5-4.5 ZA'

	print "Photos with no lens info : %d" %non_lens

	plis=[]
	for lens_tag in lens_models:
		pids = lens_models[lens_tag]
		print "Total %d photos with tag %s" %(len(pids),lens_tag)
		pli = PhotosWithLensInfo(lens_tag,pids)
		plis.append(pli)

		# flickr.photos.setTags(photo_id=pids,tags=lens_tag)
		# for pid in pids:
		# 	print pid+" ",
		# print ""


	with open(PIK,"wb") as f:
		pickle.dump(plis,f)

	import time

	for lens_tag in lens_models:
		pids = lens_models[lens_tag]
		print "Total %d photos with tag %s" %(len(pids),lens_tag)
		total_pids = len(pids)
		for i in range(total_pids):
			pid = pids[i]
			try:
				flickr.photos.setTags(photo_id=pid,tags=lens_tag)
			except :
				print "No handlers could be found for logger 'flickrapi.auth.OAuthFlickrInterface'"
				time.sleep(10)
				flickr = connect(auth_key, auth_secret)
				i=i-1
				total_pids += 1
				continue

			print pid+" ",
			if (i+1)%10==0:
				print ""
		print ""






#sets = flickr.photosets.getList(user_id=userid)
