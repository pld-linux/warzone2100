#$Revision: 1.21.2.1 $, $Date: 2008-04-19 23:52:24 $
%define		_beta	beta2
Summary:	3D realtime strategy on a future Earth
Summary(pl.UTF-8):	Gra RTS, której akcja toczy się w przyszłości
Name:		warzone2100
Version:	2.1
Release:	0.%{_beta}.1
License:	GPL v2+
Group:		X11/Applications/Games/Strategy
Source0:	http://download.gna.org/warzone/releases/2.1/%{name}-%{version}_%{_beta}.tar.bz2
# Source0-md5:	566b7b9f79d5f9b6b9b7d14b410d86e4
Patch0:		%{name}-desktop.patch
URL:		http://www.wz2100.net/
BuildRequires:	OpenAL-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	SDL-devel >= 1.1.4
BuildRequires:	SDL_net-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libjpeg-devel
BuildRequires:	libmad-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libpng-devel
BuildRequires:	perl-base
BuildRequires:	physfs-devel
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRequires:	quesoglc-devel
BuildRequires:	zip
BuildRequires:	unzip
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

%prep
%setup -q -n %{name}-%{version}_%{_beta}
%patch0 -p1

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
#%{__perl} -pi -e "s#-m32##g" makerules/common.mk
%{__perl} -pi -e "s#-m32##g" configure
%configure --with-distributor="PLD"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

install icons/%{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}
install icons/%{name}.png $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog doc/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.*
