%define api	1.0

Summary:	GStreamer Streaming-media framework plug-ins
Name:		gst-plugins-good
Version:	1.0.5
Release:	1
License:	LGPLv2+
Group:		Sound
URL:		http://gstreamer.freedesktop.org/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gst-plugins-good/%{api}/%{name}-%{version}.tar.xz

#BuildRequires:	gst-plugins-base
BuildRequires:	bzip2-devel
BuildRequires:	gettext-devel
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(check)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gdk-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libv4l1)
BuildRequires:	pkgconfig(libv4l2)
BuildRequires:	pkgconfig(orc-0.4)
BuildRequires:	pkgconfig(shout)
BuildRequires:	pkgconfig(theora)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(gudev-1.0)
%ifarch %{ix86}
BuildRequires:	nasm => 0.90
BuildRequires:	valgrind
%endif
Suggests:	%{name}-soup

%description
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plug-ins.

This package contains a set of plug-ins that are considered to have
good quality code, correct functionality, the preferred license (LGPL
for the plug-in code, LGPL or LGPL-compatible for the supporting
library). People writing elements should base their code on these
elements.

%package	jack
Summary:	GStreamer plug-in for the Jack Sound Server
Group:		Sound
BuildRequires:	pkgconfig(jack)

%description	jack
Plug-in for the JACK professional sound server.

%files	jack
%{_libdir}/gstreamer-%{api}/libgstjack.so

%package	soup
Summary:	GStreamer HTTP plugin based on libsoup
Group:		System/Libraries
Requires:	plugins
BuildRequires:	pkgconfig(libsoup-2.4)

%description	soup
Plug-in for HTTP access based on libsoup.

%files	soup
%{_libdir}/gstreamer-%{api}/libgstsouphttpsrc.so

%package	pulse
Summary:	Pulseaudio plugin for GStreamer
Group:		Sound
Requires:	plugins
BuildRequires:	pkgconfig(libpulse)

%description	pulse
This is a GStreamer audio output plugin using the Pulseaudio sound server.

%files	pulse
%{_libdir}/gstreamer-%{api}/libgstpulse.so

%package	dv
Summary:	GStreamer DV plug-in
Group:		Video
Requires:	gst-plugins-base
BuildRequires:	pkgconfig(libdv)

%description	dv
Plug-in for digital video support using libdv.

%files	dv
%{_libdir}/gstreamer-%{api}/libgstdv.so

%package	speex
Summary:	Gstreamer plugin for encoding and decoding Ogg Speex audio files
Group:		Sound
Requires:	gst-plugins-base
BuildRequires:	pkgconfig(speex)

%description	speex
Plug-Ins for creating and playing Ogg Speex audio files.

%files	speex
%{_libdir}/gstreamer-%{api}/libgstspeex.so

%package	raw1394
Summary:	GStreamer raw1394 Firewire plug-in
Group:		System/Libraries
Requires:	gst-plugins-base
BuildRequires:	pkgconfig(libavc1394)
BuildRequires:	pkgconfig(libraw1394)
BuildRequires:	pkgconfig(libiec61883)

%description	raw1394
Plug-in for digital video support using raw1394.

%files	raw1394
%{_libdir}/gstreamer-%{api}/libgst1394.so

%package	flac
Summary:	GStreamer plug-in for FLAC lossless audio
Group:		Sound
Requires:	gst-plugins-base
BuildRequires:	pkgconfig(flac)

%description	flac
Plug-in for the free FLAC lossless audio format.

%files	flac
%{_libdir}/gstreamer-%{api}/libgstflac.so

%package	aalib
Summary:	Gstreamer plugin for Ascii-art output
Group:		Video
Requires:	gst-plugins-base
BuildRequires:	aalib-devel

%description	aalib
Plugin for viewing movies in Ascii-art using aalib library.

%files	aalib
%{_libdir}/gstreamer-%{api}/libgstaasink.so

%package	caca
Summary:	Gstreamer plugin for Ascii-art output
Group:		Video
BuildRequires:	pkgconfig(caca)
Requires:	gst-plugins-base

%description	caca
Plugin for viewing movies in Ascii-art using caca library.

%files	caca
%{_libdir}/gstreamer-%{api}/libgstcacasink.so

%package	wavpack
Summary:	Gstreamer plugin for encoding and decoding WavPack audio files
Group:		Sound
Requires:	gst-plugins-base
BuildRequires:	pkgconfig(wavpack)

%description	wavpack
Plug-Ins for creating and playing WavPack audio files.

%files	wavpack
%{_libdir}/gstreamer-%{api}/libgstwavpack.so

%prep
%setup -q
%apply_patches

%build
%configure2_5x  \
	--with-package-name='ROSA %{name} package' \
	--with-package-origin='http://rosalinux.com' \
	--enable-experimental \
	--disable-dependency-tracking \
	--disable-hal
%make

%install
%makeinstall_std
%find_lang %{name}-%{api}

#blino remove development doc since we don't ship devel files
rm -rf %{buildroot}%{_docdir}/docs/plugins/html

%files -f %{name}-%{api}.lang
%doc AUTHORS COPYING README NEWS
%{_libdir}/gstreamer-%{api}/libgstalaw.so
%{_libdir}/gstreamer-%{api}/libgstalpha.so
%{_libdir}/gstreamer-%{api}/libgstalphacolor.so
%{_libdir}/gstreamer-%{api}/libgstapetag.so
%{_libdir}/gstreamer-%{api}/libgstaudiofx.so
%{_libdir}/gstreamer-%{api}/libgstaudioparsers.so
%{_libdir}/gstreamer-%{api}/libgstauparse.so
%{_libdir}/gstreamer-%{api}/libgstautodetect.so
%{_libdir}/gstreamer-%{api}/libgstavi.so
%{_libdir}/gstreamer-%{api}/libgstcairo.so
%{_libdir}/gstreamer-%{api}/libgstcutter.so
%{_libdir}/gstreamer-%{api}/libgstdebug.so
%{_libdir}/gstreamer-%{api}/libgstdeinterlace.so
%{_libdir}/gstreamer-%{api}/libgsteffectv.so
%{_libdir}/gstreamer-%{api}/libgstflv.so
%{_libdir}/gstreamer-%{api}/libgstequalizer.so
%{_libdir}/gstreamer-%{api}/libgstflxdec.so
%{_libdir}/gstreamer-%{api}/libgstgdkpixbuf.so
%{_libdir}/gstreamer-%{api}/libgstgoom.so
%{_libdir}/gstreamer-%{api}/libgstgoom2k1.so
%{_libdir}/gstreamer-%{api}/libgsticydemux.so
%{_libdir}/gstreamer-%{api}/libgstid3demux.so
%{_libdir}/gstreamer-%{api}/libgstimagefreeze.so
%{_libdir}/gstreamer-%{api}/libgstinterleave.so
%{_libdir}/gstreamer-%{api}/libgstisomp4.so
%{_libdir}/gstreamer-%{api}/libgstjpeg.so
%{_libdir}/gstreamer-%{api}/libgstlevel.so
%{_libdir}/gstreamer-%{api}/libgstmatroska.so
%{_libdir}/gstreamer-%{api}/libgstmonoscope.so
%{_libdir}/gstreamer-%{api}/libgstmulaw.so
%{_libdir}/gstreamer-%{api}/libgstmultifile.so
%{_libdir}/gstreamer-%{api}/libgstmultipart.so
%{_libdir}/gstreamer-%{api}/libgstnavigationtest.so
%{_libdir}/gstreamer-%{api}/libgstossaudio.so
%{_libdir}/gstreamer-%{api}/libgstoss4audio.so
%{_libdir}/gstreamer-%{api}/libgstpng.so
%{_libdir}/gstreamer-%{api}/libgstreplaygain.so
%{_libdir}/gstreamer-%{api}/libgstrtp.so
%{_libdir}/gstreamer-%{api}/libgstrtpmanager.so
%{_libdir}/gstreamer-%{api}/libgstrtsp.so
%{_libdir}/gstreamer-%{api}/libgstshapewipe.so
%{_libdir}/gstreamer-%{api}/libgstshout2.so
%{_libdir}/gstreamer-%{api}/libgstsmpte.so
%{_libdir}/gstreamer-%{api}/libgstspectrum.so
%{_libdir}/gstreamer-%{api}/libgsttaglib.so
%{_libdir}/gstreamer-%{api}/libgstudp.so
%{_libdir}/gstreamer-%{api}/libgstvideo4linux2.so
%{_libdir}/gstreamer-%{api}/libgstvideobox.so
%{_libdir}/gstreamer-%{api}/libgstvideocrop.so
%{_libdir}/gstreamer-%{api}/libgstvideofilter.so
%{_libdir}/gstreamer-%{api}/libgstvideomixer.so
%{_libdir}/gstreamer-%{api}/libgstwavenc.so
%{_libdir}/gstreamer-%{api}/libgstwavparse.so
%{_libdir}/gstreamer-%{api}/libgstximagesrc.so
%{_libdir}/gstreamer-%{api}/libgsty4menc.so
%dir %{_datadir}/gstreamer-%{api}/
%dir %{_datadir}/gstreamer-%{api}/presets
%{_datadir}/gstreamer-%{api}/presets/*

