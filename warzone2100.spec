Summary:	3D realtime strategy on a future Earth
Summary(pl):	Gra RTS, której akcja toczy siê w przysz³o¶ci
Name:		warzone2100
Version:	2.0.4
Release:	0.1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://download.gna.org/warzone/releases/2.0/%{name}-%{version}.tar.bz2
# Source0-md5:	84e92061d9a00405994ab7496d03a610
URL:		http://wz.rootzilla.de/site/
BuildRequires:	OpenAL-devel
BuildRequires:	SDL-devel >= 1.1.4
BuildRequires:	SDL_net-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex
BuildRequires:	physfs-devel
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
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
