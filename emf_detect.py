from rtlsdr import RtlSdr
import numpy as np
import time

assert RtlSdr is not None


def calculate_power_dB(samples: int):
    # Calculate power from IQ samples
    power = np.mean(np.abs(samples) ** 2)  # Average power
    power_dB = 10 * np.log10(power)  # Convert to dB
    return power_dB


def main():
    # Parameters
    target_freq = 21e8  # 2.1 GHz (magic number)
    lo_freq = 15e8  # 1.5 GHz (LO of Ham It Down)
    downconverted_freq = target_freq - lo_freq  # 100 MHz
    dB_threshold = -40  # Example threshold in dB (adjust as needed)
    samples_per_read = 1024  # Number of samples per capture

    # SDR configuration
    sdr = RtlSdr()
    sdr.sample_rate = 2.048e6  # Hz (common rate for RTL-SDR)
    sdr.center_freq = downconverted_freq
    sdr.gain = "auto"  # Auto gain, or set manually (e.g., 20)

    try:
        print("Monitoring signal at 2.1 GHz...")
        while True:
            # Read samples
            samples = sdr.read_samples(samples_per_read)

            # Calculate signal power in dB
            power_dB = calculate_power_dB(samples)

            # Check if power exceeds threshold
            if power_dB > dB_threshold:
                print(
                    f"Signal detected at 2.1 GHz! Power: {power_dB:.2f} dB (exceeds {dB_threshold} dB)"
                )
            else:
                print(f"Current power: {power_dB:.2f} dB (below threshold)")

            # Small delay to avoid overwhelming output
            time.sleep(0.33)

    except KeyboardInterrupt:
        print("\nStopped by user.")
    finally:
        sdr.close()
        print("SDR closed.")


if __name__ == "__main__":
    main()
