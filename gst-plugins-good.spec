%define api	1.0
%define oname	gstreamer%{api}

Summary:	GStreamer Streaming-media framework plug-ins
Name:		gst-plugins-good
Version:	1.6.3
Release:	2
License:	LGPLv2+
Group:		Sound
Url:		http://gstreamer.freedesktop.org/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gst-plugins-good/1.6/%{name}-%{version}.tar.xz

#BuildRequires:	gst-plugins-base
BuildRequires:	bzip2-devel
BuildRequires:	gettext-devel
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(cairo) >= 1.10.0
BuildRequires:	pkgconfig(cairo-gobject) >= 1.10.0
BuildRequires:	pkgconfig(check)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gdk-2.0)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0) >= 2.8.0
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gstreamer-plugins-base-%{api})
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.0.0
BuildRequires:	pkgconfig(gtk+-x11-3.0) >= 3.0.0
BuildRequires:	pkgconfig(gudev-1.0) >= 143
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libv4l1)
BuildRequires:	pkgconfig(libv4l2)
BuildRequires:	pkgconfig(orc-0.4)
BuildRequires:	pkgconfig(shout)
BuildRequires:	pkgconfig(theora)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(vpx)
BuildRequires:	pkgconfig(xdamage)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	pkgconfig(xv)
%ifarch %{ix86}
BuildRequires:	nasm => 0.90
BuildRequires:	valgrind
%endif

%description
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plug-ins.

%package -n	%{oname}-plugins-good
Group:		System/Libraries
Summary:	Sound
Suggests:	%{oname}-soup
%rename		gstreamer1.0-voip

%description -n	%{oname}-plugins-good
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

%package -n	%{oname}-jack
Summary:	GStreamer plug-in for the Jack Sound Server
Group:		Sound
BuildRequires:	pkgconfig(jack)

%description -n	%{oname}-jack
Plug-in for the JACK professional sound server.

%files -n	%{oname}-jack
%{_libdir}/gstreamer-%{api}/libgstjack.so

%package -n	%{oname}-soup
Summary:	GStreamer HTTP plugin based on libsoup
Group:		System/Libraries
Requires:	%{oname}-plugins-base
BuildRequires:	pkgconfig(libsoup-2.4)

%description -n	%{oname}-soup
Plug-in for HTTP access based on libsoup.

%files -n	%{oname}-soup
%{_libdir}/gstreamer-%{api}/libgstsouphttpsrc.so

%package -n	%{oname}-pulse
Summary:	Pulseaudio plugin for GStreamer
Group:		Sound
Requires:	%{oname}-plugins-base
BuildRequires:	pkgconfig(libpulse)

%description -n	%{oname}-pulse
This is a GStreamer audio output plugin using the Pulseaudio sound server.

%files -n	%{oname}-pulse
%{_libdir}/gstreamer-%{api}/libgstpulse.so

%package -n	%{oname}-dv
Summary:	GStreamer DV plug-in
Group:		Video
Requires:	%{oname}-plugins-base
BuildRequires:	pkgconfig(libdv)

%description -n	%{oname}-dv
Plug-in for digital video support using libdv.

%files -n	%{oname}-dv
%{_libdir}/gstreamer-%{api}/libgstdv.so

%package -n	%{oname}-speex
Summary:	Gstreamer plugin for encoding and decoding Ogg Speex audio files
Group:		Sound
Requires:	%{oname}-plugins-base
BuildRequires:	pkgconfig(speex)

%description -n	%{oname}-speex
Plug-Ins for creating and playing Ogg Speex audio files.

%files -n	%{oname}-speex
%{_libdir}/gstreamer-%{api}/libgstspeex.so

%package -n	%{oname}-raw1394
Summary:	GStreamer raw1394 Firewire plug-in
Group:		System/Libraries
Requires:	%{oname}-plugins-base
BuildRequires:	pkgconfig(libavc1394)
BuildRequires:	pkgconfig(libraw1394)
BuildRequires:	pkgconfig(libiec61883)

%description -n	%{oname}-raw1394
Plug-in for digital video support using raw1394.

%files -n	%{oname}-raw1394
%{_libdir}/gstreamer-%{api}/libgst1394.so

%package -n	%{oname}-flac
Summary:	GStreamer plug-in for FLAC lossless audio
Group:		Sound
Requires:	%{oname}-plugins-base
BuildRequires:	pkgconfig(flac)

%description -n	%{oname}-flac
Plug-in for the free FLAC lossless audio format.

%files -n	%{oname}-flac
%{_libdir}/gstreamer-%{api}/libgstflac.so

%package -n	%{oname}-aalib
Summary:	Gstreamer plugin for Ascii-art output
Group:		Video
Requires:	%{oname}-plugins-base
BuildRequires:	aalib-devel

%description -n	%{oname}-aalib
Plugin for viewing movies in Ascii-art using aalib library.

%files -n	%{oname}-aalib
%{_libdir}/gstreamer-%{api}/libgstaasink.so

%package -n	%{oname}-caca
Summary:	Gstreamer plugin for Ascii-art output
Group:		Video
BuildRequires:	pkgconfig(caca)
Requires:	%{oname}-plugins-base

%description -n	%{oname}-caca
Plugin for viewing movies in Ascii-art using caca library.

%files -n	%{oname}-caca
%{_libdir}/gstreamer-%{api}/libgstcacasink.so

%package -n %{oname}-vp8
Summary:	GStreamer VP8 plug-in
Group:		Video

%description -n %{oname}-vp8
VP8 encoding and decoding plug-in.

%files -n %{oname}-vp8
%{_libdir}/gstreamer-%{api}/libgstvpx.so

%package -n	%{oname}-wavpack
Summary:	Gstreamer plugin for encoding and decoding WavPack audio files
Group:		Sound
Requires:	%{oname}-plugins-base
BuildRequires:	pkgconfig(wavpack)

%description -n	%{oname}-wavpack
Plug-Ins for creating and playing WavPack audio files.

%files -n	%{oname}-wavpack
%{_libdir}/gstreamer-%{api}/libgstwavpack.so

%prep
%setup -q
%apply_patches

%build
export CXX=g++
export CC=gcc
%configure \
	--with-package-name='OpenMandriva %{name} package' \
	--with-package-origin="%{disturl}" \
	--enable-experimental \
	--disable-dependency-tracking \
	--disable-hal
%make

%install
%makeinstall_std
%find_lang %{name}-%{api}

#blino remove development doc since we don't ship devel files
rm -rf %{buildroot}%{_docdir}/docs/plugins/html %{buildroot}%{_datadir}/gtk-doc

%files -n %{oname}-plugins-good -f %{name}-%{api}.lang
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
%{_libdir}/gstreamer-%{api}/libgstdtmf.so
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
