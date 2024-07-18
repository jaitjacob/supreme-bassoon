Name:           bello
Version:        1.0
Release:        1%{?dist}
Summary:        A simple bash script that prints "Hello, World!"

License:        GPL
URL:            https://github.com/jaitjacob/supreme-bassoon.git
Source0:        bello.sh

BuildArch:      noarch

%description
This package contains a simple bash script that prints "Hello, World!".

%prep

%build

%install
install -D -m 0755 %{SOURCE0} %{buildroot}/usr/bin/bello

%files
/usr/bin/bello

%changelog