Summary:	Gtk frontend for GNU lilypond
Name:		denemo
Version:	0.5.5
Release:	1
License:	GPL
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(pl):	Aplikacje/D¼wiêk
Source0:	http://download.sourceforge.net/denemo/%{name}-%{version}.tar.gz
URL:		http://denemo.sourceforge.net/
Requires:	lilypond
Requires:	TiMidity++
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -q

%build
%configure

%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(644,root,root,755)
%doc NEWS* README* TODO* GOALS* DESIGN* AUTHORS*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
