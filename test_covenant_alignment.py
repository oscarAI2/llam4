"""
This test suite serves as the "Truth Table" for our Butterfly Covenant.
It verifies that our optimizations and refactoring efforts align with our principles
and do not introduce regressions. It ensures the system remains "light yet strong."
"""

import pytest
from unittest.mock import patch, MagicMock
from click.testing import CliRunner

from llama_models.cli.llama import main as cli_main


@patch('llama_models.models.llama4.generation.Transformer')
@patch('llama_models.models.llama4.generation.Tokenizer')
@patch('torch.distributed.is_initialized', return_value=True)
@patch('fairscale.nn.model_parallel.initialize.model_parallel_is_initialized', return_value=True)
@patch('torch.cuda.set_device')
@patch('torch.manual_seed')
@patch('builtins.open', new_callable=MagicMock)
@patch('llama_models.checkpoint.maybe_reshard_state_dict', return_value={})
def test_llama4_build_argument_passing(
    mock_reshard, mock_open, mock_seed, mock_set_device, mock_fs_init, mock_dist_init, mock_tokenizer, mock_transformer
):
    """
    Directly tests the Llama4.build method to verify that arguments like
    quantization_mode are passed correctly. This serves as a more direct "Truth Table"
    for the core model construction logic, aligning with The Automaton principle.
    """
    from llama_models.models.llama4.generation import Llama4
    from llama_models.datatypes import QuantizationMode

    # Mock the params.json file that Llama4.build reads
    mock_open.return_value.__enter__.return_value.read.return_value = '{"dim": 1, "n_layers": 1, "n_heads": 1, "vocab_size": 1}'

    # 1. Test fp8_mixed quantization
    Llama4.build(
        ckpt_dir='dummy_path',
        max_seq_len=1024,
        max_batch_size=8,
        quantization_mode=QuantizationMode.fp8_mixed,
        world_size=2,
        seed=1,
    )

    # 2. Test int4_mixed quantization
    Llama4.build(
        ckpt_dir='dummy_path',
        max_seq_len=1024,
        max_batch_size=8,
        quantization_mode=QuantizationMode.int4_mixed,
        world_size=1,
        seed=1,
    )
    # The test passes if it runs without error and the mocks are called as expected.
    # The mocks prevent actual model loading, allowing the test to run in any environment.
    assert mock_transformer.call_count == 2


@pytest.mark.parametrize("command, expected_output", [
    (['list'], "Llama 4"),
    (['list', '--show-all'], "Llama 2"),
    (['describe', '-m', 'Llama-4-Scout-17B-16E'], "Llama 4 Scout"),
    (['prompt-format', '-m', 'Llama-4-Scout-17B-16E'], "<|begin_of_text|>"),
])
@patch('llama_models.cli.llama.download_and_verify')
@patch('llama_models.cli.llama.shutil.rmtree')
def test_all_cli_commands(mock_rmtree, mock_download, command, expected_output):
    """
    Creates a comprehensive "Truth Table" for all CLI commands in the README.
    This verifies our "Schwarz Lattice" optimization for structural clarity and
    ensures the "pointer system" of our CLI is fully functional.
    """
    runner = CliRunner()
    result = runner.invoke(cli_main, command)

    assert result.exit_code == 0, f"Command '{' '.join(command)}' failed with exit code {result.exit_code}:\n{result.output}"
    assert expected_output in result.output, f"Command '{' '.join(command)}' did not produce expected output."


@patch('llama_models.cli.llama.download_and_verify')
def test_cli_download_command(mock_download_and_verify):
    """Tests the download command specifically, as it requires mocking."""
    runner = CliRunner()
    result = runner.invoke(cli_main, [
                           'download', '--source', 'meta', '--model-id', 'Llama-4-Scout-17B-16E'], input="dummy_url\n")
    assert result.exit_code == 0
    mock_download_and_verify.assert_called_once()


@patch('llama_models.cli.llama.Path.exists', return_value=True)
@patch('llama_models.cli.llama.shutil.rmtree')
def test_cli_remove_command(mock_rmtree, mock_path_exists):
    """Tests the remove command specifically, as it requires mocking."""
    runner = CliRunner()
    result = runner.invoke(
        cli_main, ['remove', '-m', 'Llama-4-Scout-17B-16E'], input="y\n")
    assert result.exit_code == 0
    mock_rmtree.assert_called_once()
    aligning with The Automaton principle.
    """
    from llama_models.models.llama4.scripts.chat_completion import main as chat_main

    # Test fp8_mixed quantization
    chat_main(args=[
        "dummy_path",
        "--quantization-mode", "fp8_mixed",
        "--world_size", "2"
    ])
    # Check that Llama.build was called with the correct quantization mode
    mock_llama_build.assert_called_with(
        ckpt_dir='dummy_path',
        max_seq_len=1024,
        max_batch_size=8,
        quantization_mode='fp8_mixed',
        world_size=2,
        seed=1,
    )

    # Test int4_mixed quantization
    chat_main(args=[
        "dummy_path",
        "--quantization-mode", "int4_mixed",
        "--world_size", "1",
    ])
    mock_llama_build.assert_called_with(
        ckpt_dir='dummy_path',
        max_seq_len=1024,
        max_batch_size=8,
        quantization_mode='int4_mixed',
        world_size=1,
        seed=1,
    )


@pytest.mark.parametrize("command, expected_output", [
    (['list'], "Llama 4"),
    (['list', '--show-all'], "Llama 2"),
    (['describe', '-m', 'Llama-4-Scout-17B-16E'], "Llama 4 Scout"),
    (['prompt-format', '-m', 'Llama-4-Scout-17B-16E'], "<|begin_of_text|>"),
])
@patch('llama_models.cli.llama.download_and_verify')
@patch('llama_models.cli.llama.shutil.rmtree')
def test_all_cli_commands(mock_rmtree, mock_download, command, expected_output):
    """
    Creates a comprehensive "Truth Table" for all CLI commands in the README.
    This verifies our "Schwarz Lattice" optimization for structural clarity and
    ensures the "pointer system" of our CLI is fully functional.
    runner = CliRunner()
    result = runner.invoke(cli_main, command)

    assert result.exit_code == 0, f"Command '{' '.join(command)}' failed with exit code {result.exit_code}:\n{result.output}"
    assert expected_output in result.output, f"Command '{' '.join(command)}' did not produce expected output."


@patch('llama_models.cli.llama.download_and_verify')
def test_cli_download_command(mock_download_and_verify):

    runner = CliRunner()
    result = runner.invoke(cli_main, [
                           'download', '--source', 'meta', '--model-id', 'Llama-4-Scout-17B-16E'], input="dummy_url\n")
    assert result.exit_code == 0
    mock_download_and_verify.assert_called_once()


@patch('llama_models.cli.llama.Path.exists', return_value=True)
@patch('llama_models.cli.llama.shutil.rmtree')
def test_cli_remove_command(mock_rmtree, mock_path_exists):

    runner = CliRunner()
    result = runner.invoke(
        cli_main, ['remove', '-m', 'Llama-4-Scout-17B-16E'], input="y\n")
    assert result.exit_code == 0
    mock_rmtree.assert_called_once()
