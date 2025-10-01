Summary:	3D realtime strategy on a future Earth
Summary(pl.UTF-8):	Gra RTS, której akcja toczy się w przyszłości
Name:		warzone2100
Version:	4.6.1
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games/Strategy
Source0:	https://downloads.sourceforge.net/warzone2100/releases/%{version}/%{name}_src.tar.xz
# Source0-md5:	500e1a169f39454789bfc6bdb66b7582
Patch0:		x32.patch
URL:		https://www.wz2100.net/
BuildRequires:	OpenAL-devel >= 0.0.8-4
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	SDL-devel >= 1.2
BuildRequires:	SDL_net-devel
BuildRequires:	cmake
BuildRequires:	glew-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libmad-devel
BuildRequires:	libpng-devel >= 1.2
BuildRequires:	libtheora-devel >= 0.1
BuildRequires:	libvorbis-devel >= 1.1
BuildRequires:	physfs-devel
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRequires:	quesoglc-devel
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	zip
Requires:	%{name}-data = %{version}-%{release}
Requires:	fonts-TTF-DejaVu
Requires:	gdb
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Warzone 2100 is a real-time strategy game. Although comparable to
Earth 2150 in many significant respects, it does contain aspects that
are unique. These include various radar technologies and a greater
focus on artillery and counter-battery technologies.

%description -l pl.UTF-8
Warzone 2100 jest grą strategiczną czasu rzeczywistego. Chociaż gra
bardzo przypomina grę Earth 2150, to jednak zostało do niej
wprowadzonych kilka ciekawych pomysłów. Są to między innymi rozmaite
technologie radarowe oraz większe skupienie się na technologiach
artyleryjskich oraz obronie przeciwlotniczej.

%package data
Summary:	Warzone 2100 data files
Group:		X11/Applications/Games/Strategy
BuildArch:	noarch

%description data
Warzone 2100 data files

%prep
%setup -q -n %{name}
%patch -P0 -p1

%build
mkdir -p build
cd build
%cmake ../ \
	-DCMAKE_INSTALL_DOCDIR=%{_docdir}/%{name}-%{version}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} -C build install \
        DESTDIR=$RPM_BUILD_ROOT

# unsupported
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ca_ES
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/uk_UA

%{__mv} $RPM_BUILD_ROOT{%{_iconsdir},%{_pixmapsdir}}/net.wz2100.warzone2100.png

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-%{version}
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man6/%{name}.6*
%{_desktopdir}/net.wz2100.warzone2100.desktop
%{_datadir}/metainfo/net.wz2100.warzone2100.metainfo.xml
%{_pixmapsdir}/net.wz2100.warzone2100.png

%files data
%defattr(644,root,root,755)
%{_datadir}/%{name}
