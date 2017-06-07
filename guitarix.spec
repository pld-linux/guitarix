Summary:	Linux Rock Guitar Amplifier for Jack Audio Connektion Kit
Name:		guitarix
Version:	0.35.3
Release:	1
License:	GPL v2+, GPL v3+ (abgate plugin)
Group:		Applications/Multimedia
Source0:	http://downloads.sourceforge.net/guitarix/%{name}2-%{version}.tar.xz
# Source0-md5:	d073e551b2da7d339e738f932150d581
URL:		http://guitarix.sourceforge.net/
BuildRequires:	avahi-gobject-devel
BuildRequires:	bluez-libs-devel
BuildRequires:	boost-devel >= 1.38
BuildRequires:	eigen3
BuildRequires:	fftw3-devel >= 3.1.2
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel
BuildRequires:	glibmm-devel >= 2.24.0
BuildRequires:	gperf
BuildRequires:	gtk+2-devel >= 1:2.12.0
BuildRequires:	gtkmm-devel >= 2.12.0
BuildRequires:	intltool
BuildRequires:	jack-audio-connection-kit-devel > 0.109.1
BuildRequires:	ladspa-devel
BuildRequires:	liblrdf-devel
BuildRequires:	libsndfile-devel >= 1.0.17
BuildRequires:	lilv-devel
BuildRequires:	zita-convolver-devel
BuildRequires:	zita-resampler-devel
Requires:	ladspa
Requires:	fonts-TTF-Roboto
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
%setup -q

%build
CC="%{__cc}" \
CXX="%{__cxx}" \
CFLAGS="%{rpmcflags}" \
CXXFLAGS="%{rpmcxxflags}" \
LDFLAGS="%{rpmldflags}" \
./waf configure \
	--cxxflags-release="-DNDEBUG" \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--ladspadir=%{_libdir}/ladspa

./waf build

%install
rm -rf $RPM_BUILD_ROOT

./waf install \
	--destdir=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/*.so

%find_lang %{name}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc changelog README*
%attr(755,root,root) %{_bindir}/guitarix
%attr(755,root,root) %{_libdir}/libgxw.so.0.*
%attr(755,root,root) %ghost %{_libdir}/libgxw.so.0
%attr(755,root,root) %{_libdir}/libgxwmm.so.0.*
%attr(755,root,root) %ghost %{_libdir}/libgxwmm.so.0
%attr(755,root,root) %{_libdir}/ladspa/*.so
%{_datadir}/ladspa/rdf/*.rdf
%dir %{_libdir}/lv2/gx*
%attr(755,root,root) %{_libdir}/lv2/gx*/*.so
%{_libdir}/lv2/gx*/*.ttl
%{_libdir}/lv2/gx*/modgui
%{_desktopdir}/guitarix.desktop
%{_datadir}/gx_head
%{_pixmapsdir}/*.png
