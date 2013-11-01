Summary:	GTK+/tsm/pango based terminal emulator
Summary(pl.UTF-8):	Emulator terminala oparty na bibliotekach GTK+/tsm/pango
Name:		wlterm
Version:	0
%define	snap	20131031
Release:	0.%{snap}.1
License:	MIT
Group:		Applications/Terminals
# git clone git://people.freedesktop.org/~dvdhrm/wlterm
Source0:	%{name}.tar.xz
# Source0-md5:	9c22d1bb28982eae48f2d11c359639e8
URL:		http://www.freedesktop.org/wiki/Software/kmscon/wlterm/
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a rewrite of wlterm (originally "Wayland Terminal") using
GTK+. It's meant to be simple and small and serve as example how to
use GTK+tsm+pango to write terminal emulators.

%description -l pl.UTF-8
Ten program to wlterm (początkowo "Wayland Terminal") przepisany z
użyciem GTK+. Ma być prosty i mały, i służyć jako przykład tworzenia
emulatorów terminala z użyciem bibliotek GTK+tsm+pango.

%prep
%setup -q -n wlterm

%build
# makefile is stub, need to rewrite to pass our options
%{__cc} %{rpmldflags} %{rpmcflags} %{rpmcppflags} -Wall -D_GNU_SOURCE -o wlterm \
	src/wlterm.c src/wlt_font.c src/wlt_render.c src/shl_htable.c src/shl_pty.c \
	$(pkg-config --cflags --libs gtk+-3.0 cairo pango pangocairo xkbcommon libtsm)

%install
rm -rf $RPM_BUILD_ROOT

install -D wlterm $RPM_BUILD_ROOT%{_bindir}/wlterm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING
%attr(755,root,root) %{_bindir}/wlterm
