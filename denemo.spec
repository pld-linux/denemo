#
# Conditional build:
%bcond_without	alsa		# ALSA support
%bcond_without	aubio		# AUBIO support
%bcond_without	evince		# Evince support
%bcond_without	fluidsynth	# Fluidsynth support
%bcond_with	gtk2		# GTK+ 2.x instead of 3.x
%bcond_without	jack		# JACK support
%bcond_without	portaudio	# PortAudio support
%bcond_without	portmidi	# PortMIDI support
%bcond_without	rubberband	# Rubberband support

Summary:	GTK+ frontend for GNU lilypond
Summary(pl.UTF-8):	Frontend GTK+ na GNU lilypond
Name:		denemo
Version:	2.5.0
Release:	1
License:	GPL v3+
Group:		X11/Applications/Sound
Source0:	https://ftp.gnu.org/gnu/denemo/%{name}-%{version}.tar.gz
# Source0-md5:	6382d9f4cde24feab1121963801fe32f
Patch0:		%{name}-fontsdir.patch
URL:		http://www.denemo.org/
%{?with_alsa:BuildRequires:	alsa-lib-devel >= 1.0.0}
%{?with_aubio:BuildRequires:	aubio-devel >= 0.4.0}
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
%if %{with evince}
%if %{with gtk2}
BuildRequires:	evince-devel >= 2.32
BuildRequires:	evince-devel < 3
%else
BuildRequires:	evince-devel >= 3.0
%endif
%endif
%{?with_fluidsynth:BuildRequires:	fluidsynth-devel >= 1.0.8}
%{?with_portaudio:BuildRequires:	fftw3-devel >= 3.1.2}
BuildRequires:	fontconfig-devel >= 2.2.0
BuildRequires:	gettext-tools >= 0.18
BuildRequires:	glib2-devel >= 1:2.30
%{?with_gtk2:BuildRequires:	gtk+2-devel >= 2:2.6.0}
%{!?with_gtk2:BuildRequires:	gtk+3-devel >= 3.0.0}
BuildRequires:	gtk-doc >= 1.14
%{?with_gtk2:BuildRequires:	gtksourceview2-devel >= 2.0}
%{!?with_gtk2:BuildRequires:	gtksourceview3-devel >= 3.0}
BuildRequires:	guile-devel >= 2.2
BuildRequires:	intltool >= 0.35.0
%{?with_jack:BuildRequires:	jack-audio-connection-kit-devel >= 0.102.0}
BuildRequires:	librsvg-devel >= 2.0
BuildRequires:	libsmf-devel >= 1.3
BuildRequires:	libsndfile-devel >= 1.0
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel >= 2.3.10
BuildRequires:	pkgconfig
%{?with_portaudio:BuildRequires:	portaudio-devel >= 19}
%{?with_portmidi:BuildRequires:	portmidi-devel}
%{?with_rubberband:BuildRequires:	rubberband-devel >= 1.0.8}
BuildRequires:	xorg-lib-libX11-devel
Requires:	lilypond >= 2.6
Obsoletes:	denemo-devel < 2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Denemo is a graphical music notation program written in C with GTK+.

It is intended to be used in conjunction with GNU Lilypond
(<http://lilypond.org/>), but is adaptable to other
computer-music-related purposes as well.

%description -l pl.UTF-8
Denemo to program do graficznej notacji muzycznej używający GTK+.

Jest przeznaczony do używania z GNU Lilypond (<http://lilypond.org/>),
ale może być zaadaptowany do innych celów związanych z muzyką.

%prep
%setup -q
%patch0 -p1

%build
%{__intltoolize}
%{__aclocal} -I build
%{__autoconf}
%{__autoheader}
%{__automake}
CFLAGS="%{rpmcflags} %{?debug:-DDEBUG}"
%configure \
	%{?with_alsa:--enable-alsa} \
	%{!?with_aubio:--disable-aubio} \
	%{!?with_evince:--disable-evince} \
	%{!?with_fluidsynth:--disable-fluidsynth} \
	%{?with_gtk2:--enable-gtk2} \
	%{!?with_gtk2:--enable-gtk3} \
	%{?with_jack:--enable-jack} \
	%{!?with_portaudio:--disable-portaudio} \
	%{!?with_portmidi:--disable-portmidi} \
	%{!?with_rubberband:--disable-rubberband}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS docs/{DESIGN*,GOALS,TODO}
%attr(755,root,root) %{_bindir}/annotator
%attr(755,root,root) %{_bindir}/cairo_svg2path
%attr(755,root,root) %{_bindir}/denemo
%attr(755,root,root) %{_bindir}/denemo_file_update
%attr(755,root,root) %{_bindir}/pageswitcher
%attr(755,root,root) %{_bindir}/pageturner
%attr(755,root,root) %{_bindir}/twopageturner
%{_datadir}/appdata/denemo.appdata.xml
%{_datadir}/denemo
%{_fontsdir}/denemo
%{_desktopdir}/denemo.desktop
%{_pixmapsdir}/denemo.png
