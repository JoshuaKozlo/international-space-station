# International Space Station (ISS)

Command-line app for getting the ISS location, passover time at a earth location and the number of people in space. Pulls data from [http://api.open-notify.org](http://api.open-notify.org)

## Quick Start

Clone

```
git clone https://github.com/JoshuaKozlo/international-space-station.git
```

```
cd international-space-station
```

Create virtual environment

```
python -m venv env
```

```
source env/Scripts/activate
```

## Running app

Location

```
python -m iss loc
```

Output

```
The ISS current location at 01:47 PM UTC is -43.6587 2.2442
```

Pass

```
python -m iss pass <lat> <lon>
python -m iss pass 35.2271966 -80.8462036
```

Output

```
The ISS will be overhead 35.2271966 -80.8462036 at 09:57 AM UTC for 0:03:03.152295
```

People

```
python -m iss people
```

Output

```
There are 7 aboard the ISS. They are Mike Hopkins, Victor Glover, Shannon Walker, Soichi Noguchi, Mark Vande Hei, Oleg Novitskiy, Pyotr Dubrov.
```
