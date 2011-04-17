Summary:	Linux Rock Guitar Amplifier for Jack Audio Connektion Kit
#Summary(pl.UTF-8):	-
Name:		guitarix
Version:	0.11.1
Release:	1
License:	GPL v2
Group:		Applications/Multimedia
Source0:	http://dl.sourceforge.net/guitarix/%{name}-%{version}.tar.bz2
# Source0-md5:	1c95a67c0788d6ffe609e430d4b57169
URL:		http://guitarix.sourceforge.net/
BuildRequires:	ladspa-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libsndfile-devel >= 1.0.17
BuildRequires:	gtk+2-devel
BuildRequires:	glib2-devel
BuildRequires:	gtkmm-devel
BuildRequires:	glibmm-devel
BuildRequires:	fftw3-devel >= 3.1.2
BuildRequires:	boost-devel
Requires:	ladspa
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Guitarix is a simple Linux Rock Guitar Amplifier for jack (Jack Audio
Connektion Kit) with one input and two outputs. Designed to get nice
thrash/metal/rock/blues guitar sounds. There are controls for bass,
middle, treble, gain (in/out), compressor, preamp, tube's, drive,
overdrive, oversample, anti-aliase, fuzz, balance, distortion,
freeverb, impulse response, vibrato, chorus, delay, crybaby(wah),
ampselector, tonestack, and echo. For 'pressure' in the sound you can
use the feedback and feedforward sliders.

#%description -l pl.UTF-8

%prep
%setup -q

%build
./waf configure \
	--prefix=%{_prefix} \
	--ladspadir=%{_libdir}/ladspa

./waf build

%install
rm -rf $RPM_BUILD_ROOT

./waf install \
	--destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc changelog README*
%attr(755,root,root) %{_bindir}/guitarix
%attr(755,root,root) %{_libdir}/ladspa/*.so
%{_desktopdir}/guitarix.desktop
%{_datadir}/guitarix
%{_datadir}/ladspa/rdf/guitarix.rdf
%{_pixmapsdir}/*.png
