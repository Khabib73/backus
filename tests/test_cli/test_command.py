import os
import subprocess
import sys


def test_ping(fixture_path):
    env = os.environ.copy()
    env["COVERAGE_PROCESS_START"] = "pyproject.toml"

    result = subprocess.run(
        [sys.executable, "-m", "yatl", fixture_path("ping.yatl.yaml")],
        capture_output=True,
        text=True,
        env=env,
    )

    assert result.returncode == 0, (
        f"yatl exited with code {result.returncode}\n"
        f"stdout: {result.stdout}\n"
        f"stderr: {result.stderr}"
    )
    assert not result.stderr, f"stderr should be empty, got: {result.stderr}"
    assert "Test passed" in result.stdout, (
        f"Expected 'Test passed' in stdout, got:\n{result.stdout}"
    )


def test_params(fixture_path):
    env = os.environ.copy()
    env["COVERAGE_PROCESS_START"] = "pyproject.toml"

    result = subprocess.run(
        [sys.executable, "-m", "yatl", fixture_path("params.yatl.yaml")],
        capture_output=True,
        text=True,
        env=env,
    )

    assert result.returncode == 0, (
        f"yatl exited with code {result.returncode}\n"
        f"stdout: {result.stdout}\n"
        f"stderr: {result.stderr}"
    )
    assert not result.stderr, f"stderr should be empty, got: {result.stderr}"
    assert "Test passed" in result.stdout, (
        f"Expected 'Test passed' in stdout, got:\n{result.stdout}"
    )


def test_json(fixture_path):
    env = os.environ.copy()
    env["COVERAGE_PROCESS_START"] = "pyproject.toml"

    result = subprocess.run(
        [sys.executable, "-m", "yatl", fixture_path("params.yatl.yaml")],
        capture_output=True,
        text=True,
        env=env,
    )

    assert result.returncode == 0, (
        f"yatl exited with code {result.returncode}\n"
        f"stdout: {result.stdout}\n"
        f"stderr: {result.stderr}"
    )
    assert not result.stderr, f"stderr should be empty, got: {result.stderr}"
    assert "Test passed" in result.stdout, (
        f"Expected 'Test passed' in stdout, got:\n{result.stdout}"
    )


def test_skip(fixture_path):
    env = os.environ.copy()
    env["COVERAGE_PROCESS_START"] = "pyproject.toml"

    result = subprocess.run(
        [sys.executable, "-m", "yatl", fixture_path("skip_test.yatl.yaml")],
        capture_output=True,
        text=True,
        env=env,
    )

    assert result.returncode == 0, (
        f"yatl exited with code {result.returncode}\nstdout: {result.stdout}\n"
    )


def test_empty_test_files_are_ignored(tmp_path):
    empty_test = tmp_path / "empty.yatl.yaml"
    empty_test.write_text("", encoding="utf-8")

    result = subprocess.run(
        [sys.executable, "-m", "yatl", str(tmp_path)],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "No .yatl.yaml files found" in result.stdout
    assert "Run test:" not in result.stdout
    assert "Test passed" not in result.stdout
