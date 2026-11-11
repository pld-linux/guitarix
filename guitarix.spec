
%define		nam_version	0.3.0
%define		rtneural_rev	0b0e5d0

Summary:	Linux Rock Guitar Amplifier for Jack Audio Connektion Kit
Name:		guitarix
Version:	0.47.0
Release:	1
License:	GPL v2+, GPL v3+ (abgate plugin)
Group:		Applications/Multimedia
Source0:	https://github.com/brummer10/guitarix/archive/v%{version}/%{name}2-%{version}.tar.gz
# Source0-md5:	4734f34588f96d4d8df2220c5b305e55
Source1:	https://github.com/sdatkinson/NeuralAmpModelerCore/archive/v%{nam_version}/NeuralAmpModelerCore-%{nam_version}.tar.gz
# Source1-md5:	658bb0ee3412387f2fc1e4f95e6a4bc7
Source2:	https://github.com/jatinchowdhury18/RTNeural/archive/%{rtneural_rev}/RTNeural-%{rtneural_rev}.tar.gz
# Source2-md5:	5778d0fa8242d4d16f8626e67c65c295
Patch0:		boost-1.90.patch
URL:		https://guitarix.org/
BuildRequires:	avahi-gobject-devel
BuildRequires:	bluez-libs-devel
BuildRequires:	boost-devel >= 1.42
BuildRequires:	cairo-devel
BuildRequires:	curl-devel
BuildRequires:	eigen3 >= 5.0.0
BuildRequires:	faust >= 2.79.3
BuildRequires:	fftw3-devel >= 3.1.2
BuildRequires:	fftw3-single-devel
BuildRequires:	fonts-TTF-Roboto
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel
BuildRequires:	glibmm-devel >= 2.24.0
BuildRequires:	gperf
BuildRequires:	gtk+3-devel
BuildRequires:	gtkmm3-devel
BuildRequires:	intltool
BuildRequires:	jack-audio-connection-kit-devel > 0.109.1
BuildRequires:	ladspa-devel
BuildRequires:	liblrdf-devel
BuildRequires:	libsigc++-devel
BuildRequires:	libsndfile-devel >= 1.0.17
BuildRequires:	lilv-devel
BuildRequires:	sassc
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
BuildRequires:	zita-convolver-devel >= 4.0.0
BuildRequires:	zita-resampler-devel
Requires:	fonts-TTF-Roboto
Requires:	ladspa
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoprovfiles	%{_libdir}/(ladspa|lv2)

%description
Guitarix is a simple Linux Rock Guitar Amplifier for jack (Jack Audio
Connektion Kit) with one input and two outputs. Designed to get nice
thrash/metal/rock/blues guitar sounds. There are controls for bass,
middle, treble, gain (in/out), compressor, preamp, tube's, drive,
overdrive, oversample, anti-aliase, fuzz, balance, distortion,
freeverb, impulse response, vibrato, chorus, delay, crybaby(wah),
ampselector, tonestack, and echo. For 'pressure' in the sound you can
use the feedback and feedforward sliders.


%prep
%setup -q -a1 -a2
%patch -P0 -p1

%{__mv} NeuralAmpModelerCore-%{nam_version}/* trunk/src/NAM/NeuralAmpModelerCore/
%{__mv} RTNeural-%{rtneural_rev}*/* trunk/src/RTNeural/RTNeural/

%build
cd trunk
CC="%{__cc}" \
CXX="%{__cxx}" \
CFLAGS="%{rpmcflags} -I/usr/include/eigen3" \
CXXFLAGS="%{rpmcxxflags} -std=c++17 -I/usr/include/eigen3" \
LDFLAGS="%{rpmldflags}" \
./waf configure \
	--cxxflags-release="-DNDEBUG" \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--mod-lv2 \
	--faust \
%ifarch %{ix86}
	--disable-sse \
%endif

./waf build \
	--verbose

%install
rm -rf $RPM_BUILD_ROOT

cd trunk
./waf install \
	--destdir=$RPM_BUILD_ROOT
cd -

%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/*.so

%find_lang %{name}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc trunk/changelog README.md
%attr(755,root,root) %{_bindir}/guitarix
%{_libdir}/libgxw.so.0.*
%ghost %{_libdir}/libgxw.so.0
%{_libdir}/libgxwmm.so.0.*
%ghost %{_libdir}/libgxwmm.so.0
%dir %{_libdir}/lv2/gx*
%{_libdir}/lv2/gx*/*.so
%{_libdir}/lv2/gx*/*.ttl
%{_libdir}/lv2/gx*/modgui
%{_desktopdir}/guitarix.desktop
%{_datadir}/gx_head
%{_datadir}/metainfo/org.guitarix.guitarix.metainfo.xml
%{_pixmapsdir}/*.png
