#$Revision: 1.17 $, $Date: 2007-04-08 13:13:12 $
Summary:	3D realtime strategy on a future Earth
Summary(pl.UTF-8):	Gra RTS, której akcja toczy się w przyszłości
Name:		warzone2100
Version:	2.0.6
Release:	0.1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://download.gna.org/warzone/releases/2.0/%{name}-%{version}.tar.bz2
# Source0-md5:	f831dcbc1961c6d3fe8a354439f063a2
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
#BuildRequires:	libmad-devel
BuildRequires:	libvorbis-devel
BuildRequires:	physfs-devel
BuildRequires:	zip
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
%setup -q

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
#./autogen.sh
perl -pi -e "s#-m32##g" ./makerules/common.mk
perl -pi -e "s#-m32##g" configure
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT
install debian/%{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}
install debian/%{name}.png $RPM_BUILD_ROOT%{_pixmapsdir}
install debian/%{name}.svg $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.*
