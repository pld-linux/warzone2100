%define	_rc	rc1
Summary:	3D realtime strategy on a future Earth
Summary(pl):	Gra RTS, której akcja toczy siê w przysz³o¶ci
Name:		warzone2100
Version:	2.0.5
Release:	0.%{_rc}.2
License:	GPL
Group:		X11/Applications/Games
Source0:	http://download.gna.org/warzone/releases/2.0/%{name}-%{version}_%{_rc}.tar.bz2
# Source0-md5:	ffa5e7b1b51ffa7129029a911986536f
URL:		http://www.wz2100.net/
BuildRequires:	OpenAL-devel
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.1.4
BuildRequires:	SDL_net-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libvorbis-devel
BuildRequires:	physfs-devel
BuildRequires:	zip
BuildRequires:	libjpeg-devel
#BuildRequires:	libmad-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Warzone 2100 is a real-time strategy game. Although comparable to
Earth 2150 in many significant respects, it does contain aspects that
are unique. These include various radar technologies and a greater
focus on artillery and counter-battery technologies.

%description -l pl
Warzone 2100 jest gr± strategiczn± czasu rzeczywistego. Chocia¿ gra
bardzo przypomina grê Earth 2150, to jednak zosta³o do niej
wprowadzonych kilka ciekawych pomys³ów. S± to miêdzy innymi rozmaite
technologie radarowe oraz wiêksze skupienie siê na technologiach
artyleryjskich oraz obronie przeciwlotniczej.

%prep
%setup -q -n warzone-%{version}_%{_rc}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
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
